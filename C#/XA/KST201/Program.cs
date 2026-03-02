// Title: KST201
// Created Date: 01/29/2025
// Last Modified Date: 01/29/2025
// .NET Framework version: 4.8
// Thorlabs DLL version: 1.5.2.26681
// Example Description: 
// This example demonstrates how to get a list of connected devices, set-up the communication for the Thorlabs 
// KST201 controllers, home it, and move it by 1 mm or degrees.

using System;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace KST201
{
    class Program
    {
        private static string _deviceId = "26006127";//Replace with your device serial number
        static void Main(string[] args)
        {
            SystemManager systemManager;

            //Start up XA
            try
            {
                systemManager = SystemManager.Create();
                systemManager.Startup();
            }
            catch(Exception ex)
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
                foreach (var d in devicelist)
                {
                    Console.WriteLine("Devices");
                    try
                    {
                        Console.WriteLine("{0}, Serial Number: {1}\n",
                            d.PartNumber,
                            d.Device);
                        
                    }
                    
                    catch
                    {
                        Console.WriteLine(d?.ToString() ?? "<null device>");
                    }
                }
            }
            else
            {
                Console.WriteLine("No devices found.");
            }

            //Open the KST201 device
            Kst201 device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out device);
            if (ret==false)
            {
                Console.WriteLine("Failed to open device {0}", _deviceId);
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Device {0} opened successfully", _deviceId);
            }
            try
            {
                //Enable the device
                device.SetEnableState(EnableState.Enabled,TimeSpan.FromSeconds(1));

                //Get the hardware info
                HardwareInfo hardwareInfo = device.GetHardwareInfo(TimeSpan.FromSeconds(1));
                Console.WriteLine("Device Name:{0}", hardwareInfo.PartNumber);

                //Home the device
                Console.WriteLine("Homing...");
                device.Home(TimeSpan.FromSeconds(60));
                Console.WriteLine("Homing completed.");

                //Get the connected product info to determine the unit type
                ConnectedProductInfo productInfo =device.GetConnectedProductInfo();
                Unit deviceUnit=productInfo.UnitType;

                //Get the current position
                Int32 currentPosInDeviceUnits = device.GetPositionCounter(TimeSpan.FromSeconds(5));

                //Move the device by 1 mm
                double distance = 1.0; // in mm 
                long valueInDeviceUnits = device.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
                Console.WriteLine("Moving {0} mm...", distance);
                device.Move(MoveMode.RelativeMove,(int)valueInDeviceUnits, TimeSpan.FromSeconds(30));
                Console.WriteLine("Move completed.");

                //Get the current position
                currentPosInDeviceUnits = device.GetPositionCounter(TimeSpan.FromSeconds(5));

                //Convert the device units to physical units
                UnitConversionResult currentPos =device.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
                Console.WriteLine("Current Position: {0} {1}", currentPos.Value, deviceUnit.ToString());

            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception:{0}",ex.Message);
            }
            finally
            {
                //Close the device 
                device.Disconnect();
                device.Close();

                //Shutdown XA
                systemManager.Shutdown();
                 
            }
        }
    }
}
