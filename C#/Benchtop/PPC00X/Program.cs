// Title: PPC00X
// Created Date: 02/04/2022
// Last Modified Date: 04/26/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.32
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// PPC00X Benchtop controllers.



using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericPiezoCLI.Piezo;
using Thorlabs.MotionControl.Benchtop.PrecisionPiezoCLI;

namespace PPC_Console_net_managed
{
    class Program
    {
        static void Main()
        {
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            //SimulationManager.Instance.InitializeSimulations();

            // Optionally set the piezo output voltage
            decimal voltage = 0m;

            // Change this value to reflect your device
            string serialNo = "44000001";

            try
            {
                // Tell the device manager to get the list of all devices connected to the computer, such as the controller
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                // An error occurred - see ex for details
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            // Get available Benchtop Precision Piezo Motors and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 44000123, the device prefix is 44)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopPrecisionPiezo.DevicePrefix44);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a PPC001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the BenchtopPrecisionPiezo device
            BenchtopPrecisionPiezo device = BenchtopPrecisionPiezo.CreateBenchtopPiezo(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a BenchtopPrecisionPiezo", serialNo);
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
            PrecisionPiezoChannel channel = device.GetChannel(1);
            if (channel == null)
            {
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

            // Get the current Piezo configuration 
            PiezoConfiguration piezoConfiguration = channel.GetPiezoConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            PiezoDeviceSettings currentDeviceSettings = channel.PiezoDeviceSettings as PiezoDeviceSettings;

            // display info about device
            DeviceInfo deviceInfo = channel.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Max voltage - 150
            Decimal maxVolts = channel.GetMaxOutputVoltage();

            // If a voltage is requested
            //     - 'output' voltage should match 'input' voltage - this code demonstrates chnaging/getting Voltage settings
            if ((voltage != 0) && (voltage <= maxVolts))
            {
                // Update velocity if required using real world methods
                channel.SetOutputVoltage(voltage);

                Decimal newVolts = channel.GetOutputVoltage();
                Console.WriteLine("Voltage set to {0}", newVolts);
            }

            // This section of code demonstrates how to change an I/O parameter
            PrecisionPiezoChannel piezo = channel;
            IOParams ioParams = piezo.GetIOParams();
            ioParams.ControlSrc = IOSettings.PPCIOControlModes.ExternalBNC;
            piezo.SetIOParams(ioParams);

            channel.StopPolling();
            device.Disconnect(true);

            // Uncomment this line if you are using simulations
            //SimulationManager.Instance.UninitializeSimulations();

            Console.WriteLine("Press any key to close the program.");
            Console.ReadKey();
        }
    }
}
