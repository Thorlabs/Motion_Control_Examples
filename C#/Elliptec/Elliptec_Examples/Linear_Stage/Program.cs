// Title: ELL linear stage
// Created Date: 01/09/2025
// Last Modified Date: 01/09/2025
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.6.3
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// Elliptec linear stages


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Thorlabs.Elliptec.ELLO_DLL;

namespace ELL_linear_stage
{
	internal class Program
	{
		static void Main(string[] args)
		{
			char min_address = (args.Length > 1 && ELLBaseDevice.IsValidAddress(char.ToUpper(args[1][0]))) ? char.ToUpper(args[1][0]) : '0';
			char max_address = (args.Length > 2 && ELLBaseDevice.IsValidAddress(char.ToUpper(args[2][0]))) ? char.ToUpper(args[2][0]) : 'F'; ;

			ELLDevices ellDevices = new ELLDevices();
			try
			{
				if (ELLDevicePort.Connect("COM4"))
				{
					Console.WriteLine("Discover devices");
					Console.WriteLine("================");
					// scan the port for connected devices using the given range of addresses
					List<string> devices = ellDevices.ScanAddresses(min_address, max_address);

					foreach (string device in devices)
					{
						// configure each device found
						if (ellDevices.Configure(device))
						{
							// test each device found
							Console.WriteLine("");
							Console.WriteLine("Identify device " + device[0]);
							Console.WriteLine("=================");
							ELLDevice addressedDevice = ellDevices.AddressedDevice(device[0]) as ELLDevice;

							if (addressedDevice != null)
							{
								// display the device information
								DeviceID deviceInfo = addressedDevice.DeviceInfo;
								foreach (string str in deviceInfo.Description())
								{
									Console.WriteLine(str);
								}

								// test each device according to type
								// NOTE: only a Linear stage  is shown in this example
								Console.WriteLine("");
								Console.WriteLine("Test device " + device[0]);
								Console.WriteLine("=============");

								for (char c = '1'; c <= '2'; c++)
								{
									if (addressedDevice.GetMotorInfo(c))
									{
										MotorInfo motorInfo1 = addressedDevice[c];
										foreach (string s in motorInfo1.Description())
										{
											Console.WriteLine("Output->" + s);
										}
									}
								}

								// Test the stage movement
								addressedDevice.Home(ELLBaseDevice.DeviceDirection.Linear);
								Thread.Sleep(250);
								addressedDevice.SetJogstepSize(1.0m);
								for (int i = 0; i < 10; i++)
								{
									addressedDevice.JogForward();
									Thread.Sleep(100);
								}
								break;


							}
						}
					}
					ELLDevicePort.Disconnect();

				}
			}
			catch
			{
				Console.WriteLine("Failed to connect");
				Console.ReadKey();
				ELLDevicePort.Disconnect();
				return;
			}
		}
	}
}
