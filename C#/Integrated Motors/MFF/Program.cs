// Title: MFF
// Created Date: 10/02/2023
// Last Modified Date: 10/02/2023
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.41
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// MFF Filter Flippers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Text;
using System.Threading.Tasks;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.FilterFlipperCLI;

namespace MFF10x_FilterFlipper
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Comment out if not using simulation. 
            // SimulationManager.Instance.InitializeSimulations();

            // Change serial number to match your device. 
            string serialNo = "37007009";
            
            

            try
            {
                // Tell the device manager to get the list of all devices connected to the computer.
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                // An error occurred - see ex for details.
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(FilterFlipper.DevicePrefix);

            // Create the device - MFF.
            FilterFlipper device = FilterFlipper.CreateFilterFlipper(serialNo);

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

            // Wait for the device settings to initialize - timeout 5000ms.
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
            // Start the device polling.
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained.
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored.
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled.
            Thread.Sleep(500);

            // Not used directly in example but illustrates how to obtain device settings.
            ThorlabsFilterFlipperSettings currentDeviceSettings = device.FilterFlipperDeviceSettings as ThorlabsFilterFlipperSettings;

            // Display info about device.
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Initialize moves. 
            Console.WriteLine("Motor now homing");
            device.Home(60000);
            Console.WriteLine("Homing complete");

            Console.WriteLine("Motor now moving");
            device.SetPosition(2, 60000);
            Console.WriteLine("Movement completed");

            Thread.Sleep(25);

            Console.WriteLine("Motor now moving");
            device.SetPosition(1, 60000);
            Console.WriteLine("Movement complete");

            device.StopPolling();

            device.Disconnect(true);


            Console.WriteLine("Complete. Press any key to exit");
            Console.ReadKey();
            // Comment out if not using simulation
            // SimulationManager.Instance.UninitializeSimulations();

        }
    }
}
