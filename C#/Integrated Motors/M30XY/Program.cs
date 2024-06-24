// Title: M30XY
// Created Date: 06/21/2024
// Last Modified Date: 06/21/2024
// .NET Framework version: 4.8
// Thorlabs DLL version: 1.14.47
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs M30XY Kinesis 30mm XY stage.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.DCServoCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;

namespace M30XY_Console_net_managed
{
    class Program
    {
        static void Main()
        {
            // Comment out if not using simulation
            SimulationManager.Instance.InitializeSimulations();

            // Optionally set the position for the x channel (in real units)
            decimal positionX = 10m;
            decimal positionY = 0m;

            // Get the velocity
            decimal velocityX = 0m;
            decimal velocityY = 0m;


            // Enter your device's serial number
            string serialNo = "101000001";

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

            // Get available M30XY and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 101000123, the device prefix is 101)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopDCServo.DevicePrefix101);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a M30XY or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            BenchtopDCServo device = BenchtopDCServo.CreateBenchtopDCServo(serialNo);
           
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a BenchtopDCServo", serialNo);
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

            // Connect to the two channels
            IntegratedXYStageChannel channelX = (IntegratedXYStageChannel)device.GetChannel(1);
            IntegratedXYStageChannel channelY = (IntegratedXYStageChannel)device.GetChannel(2);
            if (channelX == null)
            {
                // Connection failed
                Console.WriteLine("Channel X unavailable");
                Console.ReadKey();
                return;
            }
            if (channelY == null)
            {
                // Connection failed
                Console.WriteLine("Channel Y unavailable");
                Console.ReadKey();
                return;
            }

            // Wait for the device settings to initialize - timeout 5000ms
            if (!channelX.IsSettingsInitialized() )
            {
                try
                {
                    channelX.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }
            if (!channelY.IsSettingsInitialized())
            {
                try
                {
                    channelY.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            channelX.StartPolling(250);
            channelY.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            channelX.EnableDevice();
            channelY.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters
            // - loads configuration information into channel
            // Use the channel.DeviceID "79xxxxxx-1" to get the channel 1 settings. This is different to the serial number
            MotorConfiguration motorConfigurationX = channelX.LoadMotorConfiguration(channelX.DeviceID);
            MotorConfiguration motorConfigurationY = channelY.LoadMotorConfiguration(channelY.DeviceID);

            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsIntegratedXYStageSettings currentDeviceSettingsX = channelX.MotorDeviceSettings as ThorlabsIntegratedXYStageSettings;
            ThorlabsIntegratedXYStageSettings currentDeviceSettingsY = channelY.MotorDeviceSettings as ThorlabsIntegratedXYStageSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Home the channel
            try
            {
                Console.WriteLine("Homing device");
                channelX.Home(0);
                channelY.Home(0);
                Thread.Sleep(500);
                while (channelX.Status.IsHoming || channelY.Status.IsHoming)
                {
                    Thread.Sleep(100);
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Homed");

            // If a position is requested
            if (positionX != 0 || positionY != 0)
            {
                // Update velocity if required using real world methods - using the information obtained from configuration file
                if (velocityX != 0)
                {
                    VelocityParameters velParsX = channelX.GetVelocityParams();
                    velParsX.MaxVelocity = velocityX;
                    channelX.SetVelocityParams(velParsX);
                }
                if (velocityY != 0)
                {
                    VelocityParameters velParsY = channelY.GetVelocityParams();
                    velParsY.MaxVelocity = velocityY;
                    channelY.SetVelocityParams(velParsY);
                }

                try
                {
                    Console.WriteLine("Moving X axis to {0}", positionX);
                    Console.WriteLine("Moving Y axis to {0}", positionY);
                    channelX.MoveTo(positionX, 0);
                    channelY.MoveTo(positionY, 0);
                    Thread.Sleep(500);
                    while (channelX.Status.IsMoving || channelY.Status.IsMoving)
                    {
                        Thread.Sleep(100);
                    }
                }
                catch (Exception)
                {
                    Console.WriteLine("Failed to move to position");
                    Console.ReadKey();
                    return;
                }

                Decimal newPosX = channelX.Position;
                Decimal newPosY = channelY.Position;
                Console.WriteLine("X axis Moved to {0}", newPosX);
                Console.WriteLine("Y axis Moved to {0}", newPosY);
            }

            Thread.Sleep(500);
            channelX.StopPolling();
            channelY.StopPolling();
            device.Disconnect(true);
            Console.WriteLine("Program finishes, press any key to exit.");
            Console.ReadKey();
            // comment out if not using simulation
            SimulationManager.Instance.UninitializeSimulations();
        }
    }
}
