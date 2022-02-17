using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericPiezoCLI.StrainGauge;
using Thorlabs.MotionControl.GenericPiezoCLI.Settings;
using Thorlabs.MotionControl.TCube.StrainGaugeCLI;

namespace TSG_Console_net_managed
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
				Console.WriteLine("Usage: TSG_Console_net_managed serial_number");
				Console.ReadKey();
				return;
			}

			// Get the TSG001 serial number (e.g. 84000123)
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

            // Get available TCube StrainGauge and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 84000123, the device prefix is 84)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeStrainGauge.DevicePrefix);
			if (!serialNumbers.Contains(serialNo))
			{
				// The requested serial number is not a TSG001 or is not connected
				Console.WriteLine("{0} is not a valid serial number", serialNo);
				Console.ReadKey();
				return;
			}

			// Create the device
			TCubeStrainGauge device = TCubeStrainGauge.CreateTCubeStrainGauge(serialNo);
			if (device == null)
			{
				// An error occured
				Console.WriteLine("{0} is not a TCubeStrainGauge", serialNo);
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
			if(!device.IsSettingsInitialized())
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

		    // Get the Strain Gauge Configuration
            StrainGaugeConfiguration strainGaugeConfiguration = device.GetStrainGaugeConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            StrainGaugeDeviceSettings currentDeviceSettings = device.StrainGaugeDeviceSettings as StrainGaugeDeviceSettings;

			// Display info about device
			DeviceInfo deviceInfo = device.GetDeviceInfo();
			Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

			decimal maxTravel = device.GetMaxTravel();
			Console.WriteLine("Max Travel = {0}", maxTravel);

			device.SetDisplayMode(DisplayModeSettings.TSGDisplayModes.Voltage);
            // Needs a delay so that the current voltage can be obtained
            Thread.Sleep(250);
            decimal reading = device.Status.Reading;
            Console.WriteLine("Mode = Voltage, Reading = {0}", reading);

            device.SetDisplayMode(DisplayModeSettings.TSGDisplayModes.Position);
            // Needs a delay so that the current position can be obtained
            Thread.Sleep(250);
            reading = device.Status.Reading;
            Console.WriteLine("Mode = Position, Reading = {0}", reading);

            device.SetDisplayMode(DisplayModeSettings.TSGDisplayModes.Force);
            // Needs a delay so that the current force can be obtained
            Thread.Sleep(250);
            reading = device.Status.Reading;
            Console.WriteLine("Mode = Force, Reading = {0}", reading);

			device.StopPolling();
			device.Disconnect(true);

			Console.ReadKey();
		}

	}
}
