// Title: KDC101_Example
// Created Date: 03/05/2026
// Last Modified Date: 03/05/2023
// .NET Framework version: 4.8
// Thorlabs DLL version: 1.14.59
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KPC101 controllers.
using System;
using System.Collections.Generic;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericPiezoCLI.Piezo;
using Thorlabs.MotionControl.KCube.PiezoStrainGaugeCLI;



namespace KCP_CStest
{
    internal class Program
    {

        static void Main()
        {
            //SimulationManager.Instance.InitializeSimulations();  Uncomment for simulated device.

            // Get the test KPC101 serial number (e.g. 113000123)
            string serialNo = "113000001";

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

            // Get available KCube Piezo Strain Gauge Motors and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 113000123, the device prefix is 113)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubePiezoStrainGauge.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a KPC101 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the KCZ device
            KCubePiezoStrainGauge device = KCubePiezoStrainGauge.CreateKCubePiezoStrainGauge(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a KCubePiezoStrainGauge", serialNo);
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

            device.SetPositionControlMode(PiezoControlModeTypes.OpenLoop);

            // Max voltage - 75
            Decimal maxVolts = device.GetMaxOutputVoltage();

            Decimal voltage = 1;
            // If a voltage is requested
            if ((voltage != 0) && (voltage <= maxVolts))
            {
                // Update voltage if required using real world methods
                device.SetOutputVoltage(voltage);

                Thread.Sleep(1000);

                Decimal newVolts = device.GetOutputVoltage();
                Console.WriteLine("Voltage set to {0}", newVolts);
            }

            Console.WriteLine("Setting Zero");
            device.SetZero();
            Thread.Sleep(1000);
            Console.WriteLine("Voltage:{0}", device.GetOutputVoltage());
            Console.WriteLine("Position:{0}", device.GetPosition());

            device.SetPositionControlMode(PiezoControlModeTypes.CloseLoop);


            //Set position
            Decimal setposition = 1.5m;
            device.SetPosition(setposition);

            Thread.Sleep(1000);

            Decimal position = device.GetPosition();
            Console.WriteLine("New Position {0}", position);


            device.StopPolling();

            device.Disconnect(true);
            Console.WriteLine("Device disconnected");
            //SimulationManager.Instance.UninitializeSimulations(); uncomment for simulated device.

            Console.ReadKey();
        }
    }
}
