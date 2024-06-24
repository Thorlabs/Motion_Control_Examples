// Title: BSCX0X
// Created Date: 02/04/2022
// Last Modified Date: 04/26/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.32
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// BSCXXX Benchtop controllers.



using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.StepperMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;

namespace BSC_Console_net_managed
{
    class Program
    {
        static void Main()
        {
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            //SimulationManager.Instance.InitializeSimulations();

            // Optionally set the motor position
            decimal position = 0m;

            // Optionally set the velocity in real units
            decimal velocity = 0m;

            // Change this value to reflect your device
            string serialNo = "70174584";

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

            // Get available Benchtop Stepper Motor and check our serial number is correct - by using the device prefix
            // i.e for serial number 70000123, device prefix is 70)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopStepperMotor.DevicePrefix70);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a BSC203 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the BenchtopStepperMotor device
            BenchtopStepperMotor device = BenchtopStepperMotor.CreateBenchtopStepperMotor(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a BenchtopStepperMotor", serialNo);
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

            // Get the correct channel - channel 1
            StepperMotorChannel channel = device.GetChannel(1);
            if (channel == null)
            {
                // Connection failed
                Console.WriteLine("Channel unavailable {0}", serialNo);
                Console.ReadKey();
                return;
            }

            // Wait for the device settings to initialize - timeout 5000ms
            if (!channel.IsSettingsInitialized())
            {
                try
                {
                    channel.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device.
            channel.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            channel.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters
            //  - loads configuration information into channel
            // Use the channel.DeviceID "70xxxxxx-1" to get the channel 1 settings. This is different to the serial number
            MotorConfiguration motorConfiguration = channel.LoadMotorConfiguration(channel.DeviceID);

            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsBenchtopStepperMotorSettings currentDeviceSettings = channel.MotorDeviceSettings as ThorlabsBenchtopStepperMotorSettings;
            channel.GetSettings(currentDeviceSettings);

            currentDeviceSettings.Home.HomeVel = 50.0m;
            channel.SetSettings(currentDeviceSettings, false);
            // Display info about device
            DeviceInfo deviceInfo = channel.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);
            // Testing some stuff
            try
            {
                Console.WriteLine("Setting rotation settings...");
                channel.SetRotationModes(RotationSettings.RotationModes.RotationalUnlimited, RotationSettings.RotationDirections.Quickest);
                Console.WriteLine("Homing device");
                Home_Method2(channel);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Homed");

            Decimal[] positions = { 315.0m, 270.0m, 0.0m, 315.0m, 270.0m };
            foreach(Decimal pos in positions)
            {
                try
                {
                    Console.WriteLine("Moving to position {0}", pos);
                    Move_Method2(channel, pos);
                }
                catch (Exception)
                {
                    Console.WriteLine("Failed to Move to position {0}", pos);
                    Console.ReadKey();
                    return;
                }
            }
            //// Change the position if the set value is not 0
            //if (position != 0)
            //{
            //    // Update velocity if required using real world methods
            //    if (velocity != 0)
            //    {
            //        VelocityParameters velPars = channel.GetVelocityParams();
            //        velPars.MaxVelocity = velocity;
            //        channel.SetVelocityParams(velPars);
            //    }

            //    try
            //    {
            //        Console.WriteLine("Moving Device to {0}", position);
            //        channel.MoveTo(position, 60000);
            //    }
            //    catch (Exception)
            //    {
            //        Console.WriteLine("Failed to move to position");
            //        Console.ReadKey();
            //        return;
            //    }
            //    Console.WriteLine("Device Moved");

            //    Decimal newPos = channel.Position;
            //    Console.WriteLine("Device Moved to {0}", newPos);
            //}

            // Stop polling and disconnect
            channel.StopPolling();
            device.Disconnect(true);

            // Uncomment this line if you are using simulations
            //SimulationManager.Instance.UninitializeSimulations();

            Console.WriteLine("Press any key to close the program.");
            Console.ReadKey();
        }

        /// <summary> Home method - program execution will wait until either Home completes or the function times out. </summary>
        /// <param name="device"> The device. </param>
        public static void Home_Method1(IGenericAdvancedMotor device)
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

        /// <summary> Move method - program execution will wait until either Move completes or the function times out. </summary>
        /// <param name="device">   The device. </param>
        /// <param name="position"> The target position. </param>
        public static void Move_Method1(IGenericAdvancedMotor device, decimal position)
        {
            try
            {
                Console.WriteLine("Moving Device to {0}", position);
                device.MoveTo(position, 60000);
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

        /// <summary> Home method2 - wait for completion with callback. </summary>
        public static void Home_Method2(IGenericAdvancedMotor device)
        {
            Console.WriteLine("Homing device");
            _taskComplete = false;
            _taskID = device.Home(CommandCompleteFunction);
            while (!_taskComplete)
            {
                Thread.Sleep(500);
                StatusBase status = device.Status;
                Console.WriteLine("Device Homing {0}", status.Position);

                // will need some timeout functionality;
            }
            Console.WriteLine("Device Homed");
        }

        /// <summary> Move method - program execution will wait until either Move completes or the function times out. </summary>
        /// <param name="device">   The device. </param>
        /// <param name="position"> The target position. </param>
        

    }

}
