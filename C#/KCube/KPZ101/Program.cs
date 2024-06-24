// Title: KPZ101
// Created Date: 02/11/2022
// Last Modified Date: 02/11/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KPZ101 controllers.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericPiezoCLI.Piezo;
using Thorlabs.MotionControl.KCube.PiezoCLI;

namespace KPZ_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get parameters from command line
            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage: KPZ_Console_net_managed serial_number [voltage: (0 - 75)]");
                Console.ReadKey();
                return;
            }

            // Get the piezo output voltage
            decimal voltage = 0m;
            if (argc > 1)
            {
                voltage = decimal.Parse(args[1]);
            }

            // Get the test KPZ101 serial number (e.g. 29000123)
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

            // Get available KCube Piezo Motors and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 29000123, the device prefix is 29)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubePiezo.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a KPZ101 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the KPZ device
            KCubePiezo device = KCubePiezo.CreateKCubePiezo(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a KCubePiezo", serialNo);
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

            // Get Piezo configuration
            PiezoConfiguration piezoConfiguration = device.GetPiezoConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            PiezoDeviceSettings currentDeviceSettings = device.PiezoDeviceSettings as PiezoDeviceSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Max voltage - 75
            Decimal maxVolts = device.GetMaxOutputVoltage();

            // If a voltage is requested
            if ((voltage != 0) && (voltage <= maxVolts))
            {
                // Update voltage if required using real world methods
                device.SetOutputVoltage(voltage);

                Decimal newVolts = device.GetOutputVoltage();
                Console.WriteLine("Voltage set to {0}", newVolts);
            }

            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }
    }
}
