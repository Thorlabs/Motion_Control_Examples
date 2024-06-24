// Title: BBD30X_Init_Move
// Created Date: 04/19/2024
// Last Modified Date: 04/19/2024
// .NET Framework version: 4.8.2
// Thorlabs DLL version: 1.14.47
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// BBD Benchtop controllers and initiate a simple move.




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
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            //SimulationManager.Instance.InitializeSimulations();

            try
            {
                // Build device list
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception)
            {
                Console.WriteLine("Device list failed to build");
                return;
            }

            //Get the first available BBD300 controller
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(103);

            //Check if there was a found device. If not, close the program
            if (serialNumbers.Count > 0)
            {
                Console.WriteLine(serialNumbers[0]);
            }
            else
            {
                Console.WriteLine("No connected devices");
                return;
            }

            BenchtopBrushlessMotor controller = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serialNumbers[0]);

            if (controller != null)
            {
                //Initialize the controller
                controller.Connect(serialNumbers[0]);
                controller.GetMotherboardConfiguration(serialNumbers[0], DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);

                Brushless30XMotorChannel channel = controller.GetChannel(1) as Brushless30XMotorChannel;

                if (channel != null)
                {
                    //Initialize the channel
                    channel.Connect(serialNumbers[0]);
                    channel.WaitForSettingsInitialized(3000);
                    // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real unit parameters
                    channel.LoadMotorConfiguration(channel.DeviceID);

                    channel.StartPolling(250);
                    System.Threading.Thread.Sleep(500);
                    channel.EnableDevice();
                    System.Threading.Thread.Sleep(500);

                    HomeStage(channel);

                    channel.SetVelocityParams(5, 100);

                    MoveStage(channel, 110);

                    MoveStage(channel, 55);

                    channel.StopPolling();
                    channel.DisableDevice();

                }

                //Close the controller connection
                controller.Disconnect(false);
                Console.WriteLine("Controller Disconnected");

                // Uncomment this line if you are using simulations
                //SimulationManager.Instance.UninitializeSimulations();
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
            }
        }
    }
}

