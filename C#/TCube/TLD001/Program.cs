using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.LaserDiodeCLI;

namespace TLD_Console_net_managed
{
    class Program
    {
        /// <summary> Main entry-point for this application. </summary>
        /// <param name="args"> Array of command-line argument strings. </param>
        static void Main(string[] args)
        {
            // Get parameters from command line
            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage: TLD_Console_net_managed serial_number [Power: (0 - 5)]");
                Console.ReadKey();
                return;
            }

            // Get the required output power/current
            decimal setPoint = 100m;
            if (argc > 1)
            {
                setPoint = decimal.Parse(args[1]);
            }

            // Get the test TLD001 serial number (e.g. 64000123)
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

            // Get available TLD and check our serial number is correct  - by using the device prefix
            // (i.e. for serial number 64000123, the device prefix is 64)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeLaserDiode.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // the requested serial number is not a TLD001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeLaserDiode device = TCubeLaserDiode.CreateTCubeLaserDiode(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeLaserDiode", serialNo);
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

            // Call GetLaserDiodeConfiguration on the device to initialize the settings
            LaserDiodeConfiguration laserDiodeConfiguration = device.GetLaserDiodeConfiguration(serialNo);
            ThorlabsLaserDiodeSettings currentDeviceSettings = device.LaserDiodeDeviceSettings;

            // display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Sets the current Laser Diode to Open Loop mode
            device.SetOpenLoop();
            device.SetOn();
            Thread.Sleep(500);
            if ((setPoint > 0))
            {
                // Sets the Laser Diode current(mA)
                device.SetLaserSetPoint(setPoint);
                Console.WriteLine("Power set to {0}", device.GetLaserSetPoint());
            }
            LaserDiodeStatus status = device.Status;
            Console.WriteLine("Set Point = {0}mW, Actual Laser Diode Current = {1}mA, Actual Power = {2}mW", status.LaserSetPoint, status.ActualCurrent, status.ActualPower);

            device.SetOff();
            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }
    }
}
