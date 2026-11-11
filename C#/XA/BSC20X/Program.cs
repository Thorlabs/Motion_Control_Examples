// Title: BSC20X
// Created Date: 05/04/2026
// Last Modified Date: 09/08/2026
// .NET Core version: 8.0
// XA Version Tested: 1.9.3
// Example Description:
// This example demonstrates how to connect to a BSC20X device and channel,
// home it, and perform an absolute move of 5 mm.

using Microsoft.VisualBasic;
using System;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace BSC20X
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

            // Open the BSC20X base device.
            Bsc20x device;
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
            Bsc20xLogicalChannel channel;
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

                // Get hardware info.
                HardwareInfo hardwareInfo = channel.GetHardwareInfo(TimeSpan.FromSeconds(1));
                Console.WriteLine("Channel {0} Device Name: {1}", channel.DeviceId, hardwareInfo.PartNumber);

                // Get the connected stage info.
                ConnectedProductInfo connectedProductInfo = channel.GetConnectedProductInfo();
                Console.WriteLine("Channel {0} Stage Name: {1}", channel.DeviceId, connectedProductInfo.ProductName);

                // Home the channel.
                Console.WriteLine("Homing...");
                channel.Home(TimeSpan.FromSeconds(60));
                Console.WriteLine("Homing successful.");

                // Distance to move.
                double distance = 5.0;

                // Get the unit type from the connected actuator.
                Unit deviceUnit = connectedProductInfo.UnitType;

                // Convert the physical distance to device units.
                long valueInDeviceUnits = channel.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
                Console.WriteLine("Conversion from {0} mm successful. Value in device units: {1}", distance, valueInDeviceUnits);

                // Absolute move to 5 mm.
                Console.WriteLine("Moving to {0} {1}", distance, deviceUnit.ToString());
                channel.Move(MoveMode.Absolute, (int)valueInDeviceUnits, TimeSpan.FromSeconds(60));
                Console.WriteLine("Absolute move successful.");

                // Get the current position.
                int currentPosInDeviceUnits = channel.GetPositionCounter(TimeSpan.FromSeconds(60));
                Console.WriteLine("New current position is: {0}", currentPosInDeviceUnits);

                // Convert the device units back to physical units.
                UnitConversionResult currentPos = channel.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
                Console.WriteLine("Current Position: {0} {1}", currentPos.Value, currentPos.UnitType);
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
