// Title: TDC001
// Created Date: 02/16/2022
// Last Modified Date: 05/25/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// TDC101 controllers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.TCube.DCServoCLI;

namespace TDC_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {

            // Uncomment this line (and UnitializeSimulations at the end of the program)
            // If you are using simulated devices
            SimulationManager.Instance.InitializeSimulations();

            //Replace this string with your serial number
            string serialNo = "83000001";

            // Change this value to your desired position (in real units)
            decimal position = 0m;


            // Change this value to your desired velocity (in real units)
            decimal velocity = 0m;


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

            // Get available TCube DC Servos and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 83000123, the device prefix is 83)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeDCServo.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a TDC001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeDCServo device = TCubeDCServo.CreateTCubeDCServo(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeDCServo", serialNo);
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
            DCMotorSettings currentDeviceSettings = device.MotorDeviceSettings as DCMotorSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Home the device without a callback function
            try
            {
                Console.WriteLine("Homing device");
                device.Home(60000);
                Console.WriteLine("Device Homed");
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }


            // if a position is requested
            if (position != 0)
            {
                // Update velocity if required using real world methods
                if (velocity != 0)
                {
                    VelocityParameters velPars = device.GetVelocityParams();
                    velPars.MaxVelocity = velocity;
                    device.SetVelocityParams(velPars);
                    Thread.Sleep(500); 
                }

                // Move the device to a desired position
                try
                {
                    Console.WriteLine("Moving Device to {0}", position);
                    device.MoveTo(position, 60000);
                    Console.WriteLine("Device Moved");
                }
                catch (Exception)
                {
                    Console.WriteLine("Failed to move to position");
                    Console.ReadKey();
                    return;
                }
                

                Decimal newPos = device.Position;
                Console.WriteLine("Device Moved to {0}", newPos);
            }

            device.StopPolling();
            device.Disconnect(true);

            // Uncomment this line if you are using simulations
            SimulationManager.Instance.InitializeSimulations();
            Console.ReadKey();
        }

    }
}
