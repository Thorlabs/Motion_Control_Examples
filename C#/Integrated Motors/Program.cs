using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.IntegratedStepperMotorsCLI;

namespace LTS_Integrated_Motors
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Comment out if not using simulation
            SimulationManager.Instance.InitializeSimulations();
            // Get the motor position
            decimal position = 100;

            // Insert 
            decimal velocity = 0m;

            // Change serial number to match your device. 
            string serialNo = "45000001";

            try
            {
                // Tell the device manager to get the list of all devices connected to the computer
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                // An error occurred - see ex for details
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            // Get available Long Stage Travel and check our serial number is correct
            // (i.e. for serial number 45000123, the device prefix is 45)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(LongTravelStage.DevicePrefix);


            // Create the device - LTS
            LongTravelStage device = LongTravelStage.CreateLongTravelStage(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a LongStageTravel", serialNo);
                Console.ReadKey();
                return;
            }

            // Open a connection to the device.
            try
            {
                Console.WriteLine("Opening device {0}", serialNo);
                device.Connect(serialNo);
            }
            catch (Exception)
            {
                // Connection failed
                Console.WriteLine("Failed to open device {0}", serialNo);
                Console.ReadKey();
                return;
            }

            // Wait for the device settings to initialize - timeout 5000ms
            if (!device.IsSettingsInitialized())
            {
                try
                {
                    device.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters
            // loads configuration information into channel
            MotorConfiguration motorConfiguration = device.LoadMotorConfiguration(serialNo);

            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsIntegratedStepperMotorSettings currentDeviceSettings = device.MotorDeviceSettings as ThorlabsIntegratedStepperMotorSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Initialize moves. 
            device.Home(60000);
            device.MoveTo(position, 60000);
            device.Home(60000);
          

            device.StopPolling();
            device.Disconnect(true);


            Console.WriteLine("Complete. Press any key to exit");
            Console.ReadKey();
            // comment out if not using simulation
            SimulationManager.Instance.UninitializeSimulations();

        }

    }
}