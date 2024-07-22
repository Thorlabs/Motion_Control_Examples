// Title: TBD001
// Created Date: 02/16/2022
// Last Modified Date: 05/25/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// TBD101 controllers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.TCube.BrushlessMotorCLI;

namespace TBD_Console_net_managed
{
    class Program
    {
        /// <summary> Main entry-point for this application. </summary>
        /// <param name="args"> Array of command-line argument strings. </param>
        static void Main(string[] args)
        {


            // Get the motor position
            decimal position = 0m;

            // Get the velocity
            decimal velocity = 0m;

            // Get the TBD001 serial number (e.g. 67000123)
            string serialNo = "67000001";

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

            // Get available TCube Brushless Motor and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 67000123, the device prefix is 67)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeBrushlessMotor.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a TBD001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeBrushlessMotor device = TCubeBrushlessMotor.CreateTCubeBrushlessMotor(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeBrushlessMotor", serialNo);
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
            MotorConfiguration motorConfiguration = device.LoadMotorConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            BrushlessMotorSettings currentDeviceSettings = device.MotorDeviceSettings as BrushlessMotorSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            Home_Method1(device);
            // or 
            //Home_Method2(device);
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

        /// <summary> Move method - program execution will wait until either Move completes or the function
        /// times out. </summary>
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

        /// <summary> Move method - program execution will wait until either Move completes or the function
        /// times out. </summary>
        /// <param name="device">   The device. </param>
        /// <param name="position"> The target position. </param>
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
