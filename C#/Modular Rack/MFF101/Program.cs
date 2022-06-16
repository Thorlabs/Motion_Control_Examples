using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.FilterFlipperCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.FilterFlipper;

namespace MFF_Console_net_managed
{
    class Program
    {

        static void Main(string[] args)
        {
            // get parameters from command line

            // Get the test MFF101 serial number
            string serialNo = "37000001";

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

            // Get available Filter Flipper and check our serial number is correct
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(FilterFlipper.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a MFF101 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the FilterFlipper device
            FilterFlipper device = FilterFlipper.CreateFilterFlipper(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a FilterFlipper", serialNo);
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

            // Get the Filter Flipper settings
            FilterFlipperConfiguration currentDeviceSettings = device.GetDeviceConfiguration(serialNo, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            Home(device);

            Thread.Sleep(1000);

            // Flip mounts are 'two-position' - move to position 1
            Move(device, 1);

            Thread.Sleep(1000);

            // Flip mounts are 'two-position' - move to position 2
            Move(device, 2);

            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }

        public static void Home(FilterFlipper device)
        {
            try
            {
                Console.WriteLine("Homing device");
                device.Home(60000);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Homed");
        }
        public static void Move(FilterFlipper device, uint position)
        {
            try
            {
                Console.WriteLine("Moving Device to {0}", position);
                device.SetPosition(position, 60000);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to move to position");
                Console.ReadKey();
                return;
            }
        }
    }
}
