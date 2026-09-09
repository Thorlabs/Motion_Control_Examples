// Title: BPC30X
// Created Date: 04/24/2026
// Last Modified Date: 09/08/2026
// .NET Core version: 8.0
// XA Version Tested: 1.9.3
// Example Description:
// This example demonstrates how to connect to a BPC30X device and channel,
// zero it, set the maximum output voltage, and output a voltage.

using System;
using System.Threading;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace BPC30X
{
    class Program
    {
        // Change this line to match the serial number on your device.
        private static string _deviceId = "1234";
        // Select the channel to control ("1", "2", or "3").
        private static string _channelNumber = "1";

        static void Main(string[] args)
        {
            SystemManager systemManager;

            // Start up XA.
            try
            {
                systemManager = SystemManager.Create();
                systemManager.Startup();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
                return;
            }

            // Get the device list.
            System.Collections.Generic.IList<DeviceInfo> devicelist = systemManager.GetDeviceList();
            Console.WriteLine("Connected devices: {0}", devicelist?.Count ?? 0);
            if (devicelist != null && devicelist.Count > 0)
            {
                int index = 1;
                foreach (var d in devicelist)
                {
                    Console.Write("Device {0}: ", index);
                    try
                    {
                        Console.WriteLine("{0}, Serial Number: {1}", d.DeviceType, d.Device);
                    }
                    catch
                    {
                        Console.WriteLine(d?.ToString() ?? "<null device>");
                    }
                    index++;
                }
            }
            else
            {
                Console.WriteLine("No devices found.");
            }

            // Open the BPC30X base device.
            Bpc30x device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out device);
            if (ret == false)
            {
                Console.WriteLine("\nFail to open base unit {0}", _deviceId);
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("\nBase Unit {0} opened successfully", _deviceId);
            }

            // Open the channel.
            Bpc30xLogicalChannel channel;
            string _channelId = _deviceId + "-" + _channelNumber;
            ret = systemManager.TryOpenDevice(_channelId, "", OperatingModes.Default, out channel);
            if (ret == false)
            {
                Console.WriteLine("Fail to open channel {0}", _channelId);
                device.Close();
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Channel {0} opened successfully", channel.DeviceId);
            }

            try
            {
                // Enable the channel.
                channel.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(60));
                Console.WriteLine("Channel enabled successfully.");

                // Zero the piezo channel.
                channel.SetZero(TimeSpan.FromSeconds(60));
                Console.WriteLine("Voltage zeroed successfully.");

                // Set the maximum output voltage.
                Int16 maxOutputVoltage = 25;
                channel.SetMaxOutputVoltage(maxOutputVoltage);
                Console.WriteLine("Maximum output set successfully.");
                Thread.Sleep(200);

                // Get the maximum output voltage.
                Thorlabs.MotionControl.XA.Piezo.MaxOutputVoltageParams voltageParams = channel.GetMaxOutputVoltageParams(TimeSpan.FromSeconds(60));
                Console.WriteLine("New maximum output voltage is: {0}", voltageParams.MaxOutputVoltage);

                // Set the output voltage.
                Int16 outputVoltage = 10;
                channel.SetOutputVoltage(outputVoltage);
                Console.WriteLine("Output voltage set successfully.");
                Thread.Sleep(200);

                // Get the output voltage.
                Int16 readbackVoltage = channel.GetOutputVoltage(TimeSpan.FromSeconds(60));
                Console.WriteLine("New output voltage is: {0}", readbackVoltage);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
            }
            finally
            {
                // Close the channel.
                if (channel != null)
                    channel.Close();

                // Close the device.
                if (device != null)
                {
                    device.Disconnect();
                    device.Close();
                }
                Console.WriteLine("Channel closed.");

                // Shutdown XA.
                systemManager.Shutdown();
            }
        }
    }
}
