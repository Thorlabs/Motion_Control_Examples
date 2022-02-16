using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.InertialMotorCLI;

namespace TIM_Console_net_managed
{
    class Program
    {
        /// <summary> Main entry-point for this application. </summary>
        /// <param name="args"> Array of command-line argument strings. </param>
        static void Main(string[] args)
        {
            // Get parameters from command line
            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage: TIM_Console_net_managed serial_number");
                Console.ReadKey();
                return;
            }

            // Get the serial number (e.g. 65000123)
            string serialNo = args[0];

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

            // Get available TCube Inertial Motor and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 65000123, the device prefix is 65)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeInertialMotor.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a TSC001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeInertialMotor device = TCubeInertialMotor.CreateTCubeInertialMotor(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeInertialMotor", serialNo);
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

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Get InertialMotor device configuration
            InertialMotorConfiguration InertialMotorConfiguration = device.GetInertialMotorConfiguration(serialNo);
            ThorlabsInertialMotorSettings currentDeviceSettings = ThorlabsInertialMotorSettings.GetSettings(InertialMotorConfiguration);

            // Set the 'Step' paramaters for the Inertia Motor and download to device
            currentDeviceSettings.Drive.Channel(InertialMotorStatus.MotorChannels.Channel1).StepRate = 500;
            currentDeviceSettings.Drive.Channel(InertialMotorStatus.MotorChannels.Channel1).StepAcceleration = 100000;
            device.SetSettings(currentDeviceSettings, true, true);

            // Zero the device
            device.SetPositionAs(InertialMotorStatus.MotorChannels.Channel1, 0);

            int position = 1000;
            Move_Method1(device, InertialMotorStatus.MotorChannels.Channel1, position);
            // or
            // Move_Method2(device, InertialMotorStatus.MotorChannels.Channel1, position);

            Decimal newPos = device.GetPosition(InertialMotorStatus.MotorChannels.Channel1);
            Console.WriteLine("Device Moved to {0}", newPos);

            // Tidy up and exit
            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }

        /// <summary> Home method - program execution will wait until either Home completes or the function
        /// times out. </summary>
        /// <param name="device">   The device. </param>
        /// <param name="channel">  The channel. </param>
        /// <param name="position"> The position. </param>
        public static void Move_Method1(TCubeInertialMotor device, InertialMotorStatus.MotorChannels channel, int position)
        {
            try
            {
                Console.WriteLine("Moving Device to {0}", position);
                device.MoveTo(channel, position, 60000);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to move to position");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Moved");
        }

        private static bool _taskComplete;
        private static ulong _taskID;

        /// <summary> Command complete function. </summary>
        /// <remarks> called when a specified task completes</remarks>
        /// <param name="taskID"> Identifier for the task. </param>
        public static void CommandCompleteFunction(ulong taskID)
        {
            if ((_taskID > 0) && (_taskID == taskID))
            {
                _taskComplete = true;
            }
        }

        /// <summary> Move method - program execution will wait until either Move completes or the function
        /// times out. </summary>
        /// <param name="device">   The device. </param>
        /// <param name="channel">  The channel. </param>
        /// <param name="position"> The position. </param>
        public static void Move_Method2(TCubeInertialMotor device, InertialMotorStatus.MotorChannels channel, int position)
        {
            Console.WriteLine("Moving Device to {0}", position);
            _taskComplete = false;
            _taskID = device.MoveTo(channel, position, CommandCompleteFunction);
            while (!_taskComplete)
            {
                Thread.Sleep(500);
                int actualPosition = device.GetPosition(channel);
                Console.WriteLine("Device Moving {0}", actualPosition);

                // will need some timeout functionality;
            }
            Console.WriteLine("Device Moved");
        }
    }
}
