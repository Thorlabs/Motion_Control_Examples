using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.LaserSourceCLI;

namespace TLS_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {
            // Replace this line with your device's serial
            string serialNo = "86000001";

            // Get the required output position voltage
            decimal power = 0;
                       
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

            // Get available TLS and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 86000123, the device prefix is 86)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeLaserSource.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a TLS001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeLaserSource device = TCubeLaserSource.CreateTCubeLaserSource(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeLaserSource", serialNo);
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

            // Call GetLaserSourceConfiguration on the device to initialize the settings
            LaserSourceConfiguration laserSourceConfiguration = device.GetLaserSourceConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsLaserSourceSettings currentDeviceSettings = device.LaserSourceDeviceSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Set Laser Source Power
            device.SetDisplayUnits(DisplayModeSettings.ControlDisplayModes.MilliWatts);
            if ((power > 0))
            {
                device.SetPower(power);
                Console.WriteLine("Power set to {0}", device.GetSetPower());
            }
            device.SetOn();
            Thread.Sleep(500);
            LaserSourceStatus status = device.Status;
            Console.WriteLine("Set Power = {0}mW, Actual Power = {1}mW, Actual Current = {2}mA", status.SetPower, status.ActualPower, status.ActualCurrent);

            device.SetOff();
            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }
    }
}
