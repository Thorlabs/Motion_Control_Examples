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
            try
            {
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception)
            {
                Console.WriteLine("Device list failed to build");
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

                    channel.SetVelocityParams(5, 100);

                    MoveStage(channel, 110);

                    MoveStage(channel, 55);

                    channel.StopPolling();
                    channel.DisableDevice();

                }
                controller.Disconnect(false);
                Console.WriteLine("Controller Disconnected");
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

