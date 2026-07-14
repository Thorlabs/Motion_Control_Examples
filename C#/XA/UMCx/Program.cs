// Title: UMCX
// Created Date: 23/06/2026
// Last Modified Date: 23/06/2026
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.6.8.27431
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// UMCX controllers with a brushless stage, home it, and move it by 1 mm or degrees.

using System;
using System.Threading;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace UMC.net_testing
{
    class Program
    {
        //Change this line to match the serial number on your device (format: 121XXXXXX)
        private static string _deviceId = "121000020";
        //Select the channel to control ("1", "2", or "3")
        private static string _channelNumber = "1";

        static void Main(string[] args)
        {
            SystemManager systemManager;

            //Start up XA
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


            //Get the device list
            System.Collections.Generic.IList<DeviceInfo> devicelist = systemManager.GetDeviceList();

            // Print all connected devices
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

            //Open the UMCx device
            Umcx device;
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

            //Open the channel
            UmcxBrushlessLogicalChannel channel; //Make sure to choose the correct stage type for the channel, i.e. UmcxBrushlessLogicalChannel or UmcxStepperLogicalChannel
            string _channelId = _deviceId + "-" + _channelNumber;
            ret = systemManager.TryOpenDevice(_channelId, "", OperatingModes.Default, out channel);
            if (ret == false)
            {
                Console.WriteLine("Fail to open channel {0}", channel.DeviceId);
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Channel {0} opened successfully", channel.DeviceId);
            }

            try
            {
                //Enable the device
                channel.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(1));

                //Get the stage information
                ConnectedProductInfo connectedProductInfo = channel.GetConnectedProductInfo();
                Console.WriteLine("Channel {0} Stage Name:{1}", channel.DeviceId, connectedProductInfo.ProductName);

                //Home the device
                Console.WriteLine("Homing");
                channel.Home(TimeSpan.FromSeconds(60));
                Console.WriteLine("Home completed");

                //Set the distance. Unit: millimeters or degrees depending on the actuator
                double distance = 1;

                //Get the unit type of the actuator
                Unit deviceUnit = connectedProductInfo.UnitType;

                //Convert the distance to device unit
                long posInDeviceUnits = channel.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
                Thread.Sleep(500);

                //Move the device
                Console.WriteLine("Moving to {0} {1}", distance, deviceUnit.ToString());
                channel.Move(MoveMode.Absolute, (int)posInDeviceUnits, TimeSpan.FromSeconds(60));
                Console.WriteLine("Move completed");

                //Get the current position
                int currentPosInDeviceUnits = channel.GetPositionCounter(TimeSpan.FromSeconds(1));

                //Convert the device unit to physical unit
                UnitConversionResult currentPos = channel.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
                Console.WriteLine("Current Position: {0} {1}", currentPos.Value, currentPos.UnitType);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
            }
            finally
            {
                //Close the channel
                if (channel != null)
                    channel.Close();

                //Close the device
                if (device != null)
                {
                    device.Disconnect();
                    device.Close();
                }

                //Shutdown XA
                systemManager.Shutdown();

            }
        }
    }
}
