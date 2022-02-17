using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.TECCLI;

namespace TEC_Console_net_managed
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
                Console.WriteLine("Usage: TEC_Console_net_managed serial_number [temperature: (-45 - 145)]");
                Console.ReadKey();
                return;
            }

            // Get the temperature
            decimal temperature = 0m;
            if (argc > 1)
            {
                temperature = decimal.Parse(args[1]);
            }

            // Get the TTC001 serial number (e.g. 87000123)
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

            // Get available TCube TEC and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 87000123, the device prefix is 87)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeTEC.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // the requested serial number is not a TTC001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeTEC device = TCubeTEC.CreateTCubeTEC(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeTEC", serialNo);
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

            // Call GetTECConfiguration on the device to initialize the settings
            TECConfiguration motorConfiguration = device.GetTECConfiguration(serialNo);
            ThorlabsTECSettings currentDeviceSettings = device.TECDeviceSettings as ThorlabsTECSettings;

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            device.SetDisplayMode(DisplayModeSettings.ControlDisplayModes.ActualTemperature);
            if (temperature > 0)
            {
                device.SetTemperature(temperature);
                Console.WriteLine("Temperature set to {0}", device.GetTemperatureSet());
            }

            Thread.Sleep(500);
            TECStatus status = device.Status;
            Console.WriteLine("Set Value = {0}C, Actual Value = {1}C, Actual Current = {2}mA", status.SetValue, status.ActualValue, status.ActualCurrent);

            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }

    }
}
