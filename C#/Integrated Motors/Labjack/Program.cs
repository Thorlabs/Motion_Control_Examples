// Title: Labjack
// Created Date: 07/18/2023
// Last Modified Date: 07/18/2023
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// MLJ250 labjacks.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.IntegratedStepperMotorsCLI;


namespace ISC
{
    class Program
    {
        static void Main()
        {
            // Initialize connections with all simulated devices in the KinesisSimulator
            SimulationManager.Instance.InitializeSimulations();

            // Swap this serial number for your device's
            string serialNo = "49000001";

            // Optionally enter a position to move to
            decimal position = 0m; // In real units

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

            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(LabJack.LJ050DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a ISC000 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device - LabJack
            LabJack device = LabJack.CreateLabJack(serialNo);

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
            //  - loads configuration information into channel
            MotorConfiguration motorConfiguration = device.LoadMotorConfiguration(serialNo);

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Home the device
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
            // Move the device if the position is not 0

            if (position != 0m)
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

            Console.WriteLine("Press any key + Enter to close the program.");
            Console.ReadKey();

            // Disconnect devices and simulation manager from the KinesisSimulator
            SimulationManager.Instance.UninitializeSimulations();
        }
    }
}
