// Title: MPCX20
// Created Date: 05/18/2022
// Last Modified Date: 11/29/2023
// .NET Framework version: 4.8.0
// Thorlabs DLL version: 1.14.44
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// MPCX20 modular rack controllers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.PolarizerCLI;

namespace MPC20_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            //SimulationManager.Instance.InitializeSimulations();


            // Get the MPCx20 serial number (e.g. 38000123)
            string serialNo = "38000001";

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

            // Get available Polarizer and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 38000123, the device prefix is 38)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(Polarizer.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a MPCx20 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            Polarizer device = Polarizer.CreatePolarizer(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a Polarizer", serialNo);
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

            // Get the Polarizer settings
            DeviceConfiguration.DeviceSettingsUseOptionType settingUseOptionType = DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings;
            PolarizerConfiguration configuration = device.GetDeviceConfiguration(serialNo, settingUseOptionType);
            ThorlabsPolarizerSettings currentDeviceSettings = device.PolarizerDeviceSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            for (PolarizerPaddles paddle = PolarizerPaddles.Paddle1; paddle <= PolarizerPaddles.Paddle3; paddle++)
            {
                Home(device, paddle);

                Thread.Sleep(1000);

                Move(device, paddle, 30);

                Thread.Sleep(1000);

                Move(device, paddle, 90);
            }

            device.StopPolling();
            device.Disconnect(true);

            // Uncomment this line if you are using simulations
            //SimulationManager.Instance.UninitializeSimulations();

            Console.ReadKey();
        }

        public static void Home(Polarizer device, PolarizerPaddles paddle)
        {
            try
            {
                Console.WriteLine("Homing device");
                device.Home(paddle, 60000);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Homed");
        }

        public static void Move(Polarizer device, PolarizerPaddles paddle, decimal position)
        {
            try
            {
                Console.WriteLine("Moving Device to {0}", position);
                device.MoveTo(position, paddle, 60000);
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

