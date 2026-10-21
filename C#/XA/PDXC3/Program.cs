// Title: PDXC3
// Created Date: 07/010/2026
// Last Modified Date: 07/10/2026
// .NET Framework version: 4.8
// Thorlabs DLL version: XA version 1.12.0
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// PDXC3 controllers with one channel and move the actuator in open loop mode.
// The example also shows how to get the current position of the actuator.

using System;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace PDXC3
{
    internal class Program
    {
        //Change this line to match the serial number on your device (format: 103XXXXXX)
        private static string _deviceId = "129000001";
        //Select the channel to control ("1", "2", or "3")
        private static byte _channelNumber = 1;

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

            //Uncomment this part(and systemManager.RemoveSimulation(bbd303Simulation) at the end on Main)
            //If you are using a simulated device
            /*
            string PDXC3Simulation = @"{
                ""PartNumber"": ""PDXC3"",
                ""SerialNumber"": ""129000001"",
                ""Channels"": 
                [{ ""BayNumber"": ""1"",    
                   ""SerialNumber"": ""104000001"",    
                   ""ActuatorType"": ""PDX1""},
                 {
                   ""BayNumber"": ""2"",    
                   ""SerialNumber"": ""104000001"",    
                   ""ActuatorType"": ""PDX1""},
                 {
                   ""BayNumber"": ""3"",    
                   ""SerialNumber"": ""104000001"",    
                   ""ActuatorType"": ""PDX1""}]}";

            systemManager.CreateSimulation(PDXC3Simulation);
            */

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

            //Open the PDXC3 device
            Pdxc3 parent_device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out parent_device);
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
                Pdxc3Subchannel channel;
                //string _channelId = _deviceId + "-" + _channelNumber;
                channel = (Pdxc3Subchannel)parent_device.GetSubchannel(_channelNumber);
                try { 

                channel.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(1));

                channel.SetPositionControlMode(Thorlabs.MotionControl.XA.Piezo.PositionControlMode.OpenLoop, TimeSpan.FromSeconds(1));

                Thorlabs.MotionControl.XA.PiezoInertialMotor.JogParams jogParams = channel.GetJogParams(TimeSpan.FromSeconds(1));
                jogParams.OpenLoopStepSize = 100;
                channel.SetJogParams(jogParams);
                channel.Move(MoveMode.JogForward,200, TimeSpan.FromSeconds(1));

                int currentPos=channel.GetCurrentPosition(TimeSpan.FromSeconds(1));
                Console.WriteLine("Current Position: {0}", currentPos);

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
                if (parent_device != null)
                {
                    parent_device.Disconnect();
                    parent_device.Close();
                    Console.WriteLine("Device diconnected");
                }

                //Uncomment this line if you are using Simulations
                //systemManager.RemoveSimulation(PDXC3Simulation);

                //Shutdown XA
                systemManager.Shutdown();

            }
        }

    }
}

