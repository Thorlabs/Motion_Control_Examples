// Title: BBD30X_Ethernet
// Created Date: 04/19/2024
// Last Modified Date: 04/19/2024
// .NET Framework version: 4.8.2
// Thorlabs DLL version: 1.14.47
// Example Description: 
// This example demonstrates how to set-up the ethernet communication for the Thorlabs 
// BBD Benchtop controllers.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;

namespace BBD302_Init_Move
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string startIP = "   "; // use the IP address of the start fo the scan
            string stopIP = "  ";  // use the IP address of the start fo the scan
            List<string> IPlist = DeviceManagerCLI.ScanEthernetRange(startIP, stopIP, 40303, 600000);
            Console.WriteLine(IPlist[0]);
            DeviceManagerCLI.CreateManualDeviceEntry(IPlist[0]);
            try
            {
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception)
            {
                Console.WriteLine("Device list failed to build");
                Console.ReadLine();
                return;
            }

            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(103);

            if (serialNumbers.Count > 0)
            {
                Console.WriteLine(serialNumbers[0]);
            }
            else
            {
                Console.WriteLine("No connected devices");
                Console.ReadLine();
                return;
            }


            BenchtopBrushlessMotor controller = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serialNumbers[0]);

            if (controller != null)
            {
                controller.Connect(serialNumbers[0]);
                controller.GetMotherboardConfiguration(serialNumbers[0], DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);

                Brushless30XMotorChannel channel = controller.GetChannel(1) as Brushless30XMotorChannel;

                if (channel != null)
                {
                    channel.Connect(serialNumbers[0]);
                    channel.WaitForSettingsInitialized(3000);
                    channel.LoadMotorConfiguration(channel.DeviceID);

                    channel.StartPolling(250);
                    System.Threading.Thread.Sleep(500);
                    channel.EnableDevice();
                    System.Threading.Thread.Sleep(500);

                    HomeStage(channel);
                    System.Threading.Thread.Sleep(500);

                    channel.SetVelocityParams(20, 100);

                    MoveStage(channel, 100);
                    System.Threading.Thread.Sleep(500);

                    MoveStage(channel, 55);
                    System.Threading.Thread.Sleep(500);

                    channel.StopPolling();
                    channel.DisableDevice();

                }
                controller.Disconnect(false);
                Console.WriteLine("Controller Disconnected");
                Console.ReadLine();
                DeviceManagerCLI.DeleteManualDeviceEntry(IPlist[0]);
            }
        }

        public static void HomeStage(Brushless30XMotorChannel channel)
        {
            try
            {
                Console.WriteLine("Home started");
                channel.Home(60000);
                Console.WriteLine("Home finished");
            }
            catch (Exception)
            {
                Console.WriteLine("Home was not able to complete");
                Console.ReadLine();
            }
        }

        public static void MoveStage(Brushless30XMotorChannel channel, Decimal position)
        {
            try
            {
                Console.WriteLine("Move started");
                channel.MoveTo(position, 60000);
                Console.WriteLine("Move Finsihed");
            }
            catch (Exception)
            {
                Console.WriteLine("Move was not able to complete");
                Console.ReadLine();
            }
        }
    }
}