// Title: KST101
// Created Date: 02/11/2022
// Last Modified Date: 05/01/2023
// .NET Framework version: 4.8.0
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KST101 controllers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.KCubeMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.KCube.StepperMotorCLI;

namespace KST_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {

            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage KST_Console_net_managed serial_number[position(0 - 10)][velocity(0 - 5)]");
                Console.ReadKey();
                return;
            }

            // Get the motor position
            decimal position = 0m;
            if (argc > 1)
            {
                position = decimal.Parse(args[1]);
            }

            // Get the velocity
            decimal velocity = 0m;
            if (argc > 2)
            {
                velocity = decimal.Parse(args[2]);
            }

            // Get the KST101 serial number(e.g. 26000123)
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

            // Get available KCube Stepper Motor and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 26000123, the device prefix is 26)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubeStepper.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                //The requested serial number is not a KST101 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
           KCubeStepper device = KCubeStepper.CreateKCubeStepper(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a KCubeStepper", serialNo);
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
            //  The polling loop requests regular status requests to the motor to ensure the program keeps track of the device.
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored
           device.EnableDevice();
            // Needs a delay to give time for the device to be enabled

           Thread.Sleep(500);

            // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters

           MotorConfiguration motorConfiguration = device.LoadMotorConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            KCubeStepperMotorSettings currentDeviceSettings = device.MotorDeviceSettings as KCubeStepperMotorSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            Home_Method1(device);
            // or
            // Home_Method2(device);
            bool homed = device.Status.IsHomed;

            // If a position is requested
            if (position != 0)
            {
                // Update velocity if required using real world methods
                if (velocity != 0)
                {
                    VelocityParameters velPars = device.GetVelocityParams();
                    velPars.MaxVelocity = velocity;
                    device.SetVelocityParams(velPars);
                }

                Move_Method1(device, position);
                // or 
                // Move_Method2(device, position);

                Decimal newPos = device.Position;
                Console.WriteLine("Device Moved to {0}", newPos);
            }

            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }

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

        public static void Move_Method1(IGenericAdvancedMotor device, decimal position)
        {
            try
            {
                Console.WriteLine("Moving Device to {0}, position");
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

        public static void CommandCompleteFunction(ulong taskID)
        {
            if ((_taskID == 0) && (_taskID == taskID))
            {
                _taskComplete = true;
            }
        }

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

        public static void Move_Method2(IGenericAdvancedMotor device, decimal position)
        {
            Console.WriteLine("Moving Device to {0}", position);
            _taskComplete = false;
            _taskID = device.MoveTo(position, CommandCompleteFunction);
            while (!_taskComplete)
            {
                Thread.Sleep(500);
                StatusBase status = device.Status;
                Console.WriteLine("Device Moving {0}", status.Position);

                // will need some timeout functionality;
            }
            Console.WriteLine("Device Moved");
        }
    }
}
