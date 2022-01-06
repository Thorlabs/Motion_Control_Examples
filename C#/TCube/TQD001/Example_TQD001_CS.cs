using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.TCube.QuadCLI;

namespace TQD_Console_net_managed
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
				Console.WriteLine("Usage: TQD_Console_net_managed serial_number [Horz position: (0 - 10)] [Vert position: (0 - 10)]");
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

			// Get the TQD001 serial number (e.g. 89000123)
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

            // Get available TCubeQuad and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 89000123, the device prefix is 89)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(TCubeQuad.DevicePrefix);
			if (!serialNumbers.Contains(serialNo))
			{
				// The requested serial number is not a TQD001 or is not connected
				Console.WriteLine("{0} is not a valid serial number", serialNo);
				Console.ReadKey();
				return;
			}

			// Create the device
			TCubeQuad device = TCubeQuad.CreateTCubeQuad(serialNo);
			if (device == null)
			{
				// An error occured
				Console.WriteLine("{0} is not a TCubeQuad", serialNo);
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

			// Get Quad Configuration
			QuadConfiguration quadTrakConfiguration = device.GetQuadConfiguration(serialNo);
            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsQuadSettings currentDeviceSettings = device.QuadDeviceSettings;

			// Display info about device
			DeviceInfo deviceInfo = device.GetDeviceInfo();
			Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Set position in Open Loop mode
            device.SetOperatingMode(QuadStatus.OperatingModes.OpenLoop);
			if((hPos1 > 0) && (vPos1 > 0))
			{
				device.SetPosition(new QuadPosition(hPos1, vPos1));
			}

			Thread.Sleep(500);

            QuadPosition position = device.GetDemandedPosition();
			Console.WriteLine("Demanded Position = ({0},{1})", position.X, position.Y);
			QuadStatus status = device.Status;
			Console.WriteLine("Actual Position = ({0},{1})", status.PositionDifference.X, status.PositionDifference.Y);

			device.StopPolling();
			device.Disconnect(true);

			Console.ReadKey();
		}
	}
}
