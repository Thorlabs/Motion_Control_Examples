// Title: KNA101
// Created Date: 02/11/2022
// Last Modified Date: 02/11/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KNA101 controllers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericNanoTrakCLI;
using Thorlabs.MotionControl.GenericNanoTrakCLI.ControlParameters;
using Thorlabs.MotionControl.GenericNanoTrakCLI.KCube;
using Thorlabs.MotionControl.KCube.NanoTrakCLI;

namespace KNA_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get parameters from command line
            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage: KNA_Console_net_managed serial_number [Horz position: (0 - 10)] [Vert position: (0 - 10)]");
                Console.ReadKey();
                return;
            }

            // Get the required output position voltage
            double hPos1 = 0;
            double vPos1 = 0;
            if (argc > 2)
            {
                hPos1 = double.Parse(args[1]);
                vPos1 = double.Parse(args[2]);
            }

            // Get the KNA101 serial number (e.g. 57000123)
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

            // Get available KCube NanoTrak and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 57000123, the device prefix is 57)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubeNanoTrak.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a KNA101 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            KCubeNanoTrak device = KCubeNanoTrak.CreateKCubeNanoTrak(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a KCubeNanoTrak", serialNo);
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

            // Get NanoTrak device Configuration
            NanoTrakConfiguration nanoTrakConfiguration = device.GetNanoTrakConfiguration(serialNo);
            KCubeNanoTrakDeviceSettings currentDeviceSettings = device.NanoTrakDeviceSettings as KCubeNanoTrakDeviceSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // 'Scan circle' - sine/cosine output voltages result in circular positioning
            // HomeCircle() - Move the scan circle to the defined home position
            // HVPosition - structure containg Hor/Vert pos.
            // TIA : Transient Impedence Amplifier - automatic range selected
            device.SetMode(NanoTrakStatusBase.OperatingModes.Tracking);
            if ((hPos1 > 0) && (vPos1 > 0))
            {
                device.SetCircleHomePosition(new HVPosition(hPos1, vPos1));
                device.HomeCircle();
            }
            device.SetTIARangeMode(TIARangeModes.AutoRangeAtSelected, TIAOddOrEven.All);

            Thread.Sleep(500);
            KTIAReading reading = device.GetReading();
            Console.WriteLine("Voltage set to {0} volts", reading.AbsoluteReading.ToString());

            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }
    }
}
