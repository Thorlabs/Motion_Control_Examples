using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.SolenoidCLI;

namespace TSC_Console_net_managed
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
                Console.WriteLine("Usage: TSC_Console_net_managed serial_number");
                Console.ReadKey();
                return;
            }

            // Get the TSC001 serial number (e.g. 85000123)
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

            // Get available TCube Solenoid and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 85000123, the device prefix is 85)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeSolenoid.DevicePrefix);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a TSC001 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            TCubeSolenoid device = TCubeSolenoid.CreateTCubeSolenoid(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a TCubeSolenoid", serialNo);
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

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Get Solenoid Configuration
            SolenoidConfiguration solenoidConfiguration = device.GetSolenoidConfiguration(serialNo);
            ThorlabsTCubeSolenoidSettings currentDeviceSettings = ThorlabsTCubeSolenoidSettings.GetSettings(solenoidConfiguration);

            // Set the number of cycles to 10 (means solenoid on/off 10 times) and download this value to device
            currentDeviceSettings.Cycle.NumberOfCycles = 10;
            device.SetSettings(currentDeviceSettings, true, true);

            // Start running in continuous mode
            device.SetOperatingMode(SolenoidStatus.OperatingModes.AutoToggle);
            device.SetOperatingState(SolenoidStatus.OperatingStates.Active);

            // Wait for solenoid to finish the active cycle
            Thread.Sleep(500);
            while (device.GetOperatingState() == SolenoidStatus.OperatingStates.Active)
            {
                Thread.Sleep(500);
            }

            // Tidy up and exit
            device.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }

    }
}
