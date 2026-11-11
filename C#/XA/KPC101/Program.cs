// Title: KPC101 Openloop
// Created Date: 05/19/2026
// Last Modified Date: 09/08/2026
// .NET Core version: 8.0
// XA Version Tested: 1.9.3
// Example Description:
// This example demonstrates how to connect to a KPC101 piezo controller,
// zero it, set open-loop position control mode, output a voltage, and read it back.

using System;
using System.Threading;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace KPC101
{
    class Program
    {
        // Change this line to match the serial number on your device.
        private static string _deviceId = "1234";

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

            // Open the KPC101 device.
            Kpc101 device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out device);
            if (ret == false)
            {
                Console.WriteLine("Failed to open device {0}", _deviceId);
                Console.WriteLine("Possible causes: device is turned off, not connected, or serial number is incorrect.");
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Device {0} opened successfully", _deviceId);
            }

            try
            {
                // Enable the device.
                device.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(60));
                Console.WriteLine("Device enabled successfully.");

                // Zero the piezo.
                device.SetZero(TimeSpan.FromSeconds(60));
                Console.WriteLine("Voltage zeroed successfully.");

                // Set open-loop position control mode.
                device.SetPositionControlMode(Thorlabs.MotionControl.XA.Piezo.PositionControlMode.OpenLoop, TimeSpan.FromSeconds(60));
                Console.WriteLine("Set open loop mode successfully.");

                // Set the output voltage.
                Int16 outputVoltage = 10;
                device.SetOutputVoltage(outputVoltage);
                Console.WriteLine("Output voltage set successfully.");
                Thread.Sleep(200);

                // Get the output voltage.
                Int16 readbackVoltage = device.GetOutputVoltage(TimeSpan.FromSeconds(60));
                Console.WriteLine("New output voltage is: {0}", readbackVoltage);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
            }
            finally
            {
                // Close the device.
                if (device != null)
                {
                    device.Disconnect();
                    device.Close();
                }
                Console.WriteLine("Device closed.");

                // Shutdown XA.
                systemManager.Shutdown();
            }
        }
    }
}
