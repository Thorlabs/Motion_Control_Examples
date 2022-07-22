using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.DeviceManagerCLI.ControlParameters;

namespace BBD30X_Synch_Move
{
    class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            SimulationManager.Instance.InitializeSimulations();


            // Serial number for Benchtop Brushless Motor (Example)
            // Change this line to match your device
            string serialNo = "103000001";

            try
            {
                // Build device list (necessary for operation)
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            // Get available Benchtop Brushless Motor and check our serial number is correct
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopBrushlessMotor.DevicePrefix103);
            if (!serialNumbers.Contains(serialNo))
            {
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device and check it is the correct type
            BenchtopBrushlessMotor device = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serialNo);
            if (device == null)
            {
                Console.WriteLine("{0} is not a BenchtopBrushlessMotor", serialNo);
                Console.ReadKey();
                return;
            }

            // Open device
            Console.WriteLine("Opening device {0}", serialNo);
            device.Connect(serialNo);
            bool connected = device.IsConnected;
            if (!connected)
            {
                Console.WriteLine("Failed to open device {0}", serialNo);
                Console.ReadKey();
                return;
            }


            // Get Channels one and two
            Brushless30XMotorChannel chan1 = device.GetChannel(1) as Brushless30XMotorChannel;
            Brushless30XMotorChannel chan2 = device.GetChannel(2) as Brushless30XMotorChannel;
            if (chan1 == null || chan2 == null)
            {
                Console.WriteLine("One or both channels failed to initialize");
                Console.ReadKey();
                return;
            }

            // Make sure settings are initialized
            if (!chan1.IsSettingsInitialized() || !chan2.IsSettingsInitialized())
            {
                chan1.WaitForSettingsInitialized(3000);
                chan2.WaitForSettingsInitialized(3000);
            }

            // Enable Channels and start polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device.
            chan1.StartPolling(250);
            chan2.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            chan1.EnableDevice();
            chan2.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Load the motor configuration for each channel
            MotorConfiguration chan1Config = chan1.LoadMotorConfiguration(serialNo);
            MotorConfiguration chan2Config = chan2.LoadMotorConfiguration(serialNo);

            BrushlessMotorSettings chan1Settings = chan1.MotorDeviceSettings as BrushlessMotorSettings;
            BrushlessMotorSettings chan2Settings = chan2.MotorDeviceSettings as BrushlessMotorSettings;

            // Update the settings for each channel.
            // This ensures the device unit to real value conversion is correct
            chan1Config.DeviceSettingsName = "MLS203";
            chan2Config.DeviceSettingsName = "MLS203";

            // Get the device unit converter
            chan1Config.UpdateCurrentConfiguration();
            chan2Config.UpdateCurrentConfiguration();

            chan1.SetSettings(chan1Settings, false); // False won't persist to device
            chan2.SetSettings(chan2Settings, false);

            // Home both channels
            Console.WriteLine("Homing Channels");
            try
            {
                chan1.Home(60000); // 60 second timeout
                chan2.Home(60000);
            }
            catch (DeviceException ex)
            {
                Console.WriteLine("Failed to home");
                Console.ReadKey();
                return;
            }


            // Get the Synchronous device object from the device
            BrushlessMotorSyncController syncController = device.GetSyncController();

            // Set the channel Mask:
            ushort channelMask = 0x01 + 0x02; // For channels 1 and 2

            // Create new sync movement section and assign it
            MultiChannelMoveArraySection syncSection = new MultiChannelMoveArraySection();

            syncSection.ArrayID = 1;
            syncSection.Channels = channelMask;
            syncSection.StartIndex = 0; // Used if there are more than 256 pos


            /* CREATING THE SYNCHRONOUS POSITION ARRAY
             * 
             * The sync Array is a 1D array containing positions and time
             * Each triplet in the array consists of 3 values:
             * Time, Channel 1 Position, Channel 2 Position
             * Because it is not a 2D array, care must be taken when setting the NumberOfPoints
             * The easiest way of doing so is to take the total length of the array and divide by 3
             * 
             * Positions are set in device units.
             */
            uint[] syncArray = {  10, 1000, 1000 ,
                                  20, 2000, 2000 ,
                                  30, 3000, 3000 ,
                                  40, 4000, 4000 ,
                                  50, 5000, 5000
            };


            syncSection.TimePositions = syncArray;
            syncSection.NumberOfPoints = (ushort)(syncArray.Length / 3);

            syncController.SetMultiChannelMoveArraySection(syncSection);

            Thread.Sleep(500); // Allow time for the device to update

            syncController.StartMultiChannelMoveArray(1, channelMask); // Array 1

            Thread.Sleep(60000);

            chan1.StopPolling();
            chan2.StopPolling();

            chan1.DisableDevice();
            chan2.DisableDevice();

            chan1.Disconnect(true);
            chan2.Disconnect(true);

            device.Disconnect(true);

            // Uncomment this line if you are using simulations
            SimulationManager.Instance.UninitializeSimulations();

            Console.WriteLine("Press any key to end the program");
            Console.ReadKey();
            return;
        }
    }
}
