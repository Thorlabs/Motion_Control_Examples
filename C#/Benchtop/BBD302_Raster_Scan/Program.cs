using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;

namespace BBD302_Raster_Scan
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
                Console.WriteLine("List fialed to build");
                return;
            }

            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(103);
            if (serialNumbers.Count > 0)
            {
                Console.WriteLine("Found Device: " + serialNumbers[0]);
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

                Brushless30XMotorChannel xAxis = controller.GetChannel(1) as Brushless30XMotorChannel;
                Brushless30XMotorChannel yAxis = controller.GetChannel(2) as Brushless30XMotorChannel;

                if (xAxis != null && yAxis != null)
                {
                    xAxis.Connect(serialNumbers[0]);
                    xAxis.WaitForSettingsInitialized(3000);
                    xAxis.LoadMotorConfiguration(xAxis.DeviceID);

                    yAxis.Connect(serialNumbers[0]);
                    yAxis.WaitForSettingsInitialized(3000);
                    yAxis.LoadMotorConfiguration(yAxis.DeviceID);

                    xAxis.StartPolling(250);
                    Thread.Sleep(500);
                    xAxis.EnableDevice();
                    Thread.Sleep(500);

                    yAxis.StartPolling(250);
                    Thread.Sleep(500);
                    yAxis.EnableDevice();
                    Thread.Sleep(500);

                    HomeStage(xAxis);
                    HomeStage(yAxis);

                    xAxis.SetJogVelocityParams(200, 1000);
                    xAxis.SetVelocityParams(200, 1000);

                    yAxis.SetJogVelocityParams(200, 1000);
                    yAxis.SetVelocityParams(200, 1000);

                    Decimal startX = 25;
                    Decimal startY = 50;

                    Decimal endX = 75;
                    Decimal endy = 25;

                    int numberOfXPoints = 8;
                    int numberOfRows = 4;

                    xAxis.SetJogStepSize(Math.Abs(endX - startX) / numberOfXPoints);
                    yAxis.SetJogStepSize(Math.Abs(endy - startY) / numberOfRows);

                    MotorDirection xDirection = MotorDirection.Forward;
                    MotorDirection yDirection = MotorDirection.Forward;

                    if (endX < startX)
                    {
                        xDirection = MotorDirection.Backward;
                    }
                    if (endy < startY)
                    {
                        yDirection = MotorDirection.Backward;
                    }

                    MoveStage(xAxis, startX);
                    MoveStage(yAxis, startY);

                    for (int i = 0; i < numberOfRows + 1; i++)
                    {
                        if (i != 0)
                        {
                            JogStage(yAxis, yDirection);
                        }
                        for (int j = 0; j < numberOfXPoints; j++)
                        {
                            JogStage(xAxis, xDirection);
                            Thread.Sleep(250);
                        }
                        Console.WriteLine("Row finished scanning in the {0} direction", xDirection.ToString());

                        if (xDirection == MotorDirection.Forward)
                        {
                            xDirection = MotorDirection.Backward;
                        }
                        else
                        {
                            xDirection = MotorDirection.Forward;
                        }
                    }

                    xAxis.StopPolling();
                    xAxis.DisableDevice();
                    yAxis.StopPolling();
                    yAxis.DisableDevice();

                }
                controller.Disconnect(false);
                Console.WriteLine("Controller Disconnected");
            }
        }

        public static void HomeStage(Brushless30XMotorChannel channel)
        {
            try
            {
                Console.WriteLine("home started");
                channel.Home(60000);
            }
            catch (Exception)
            { Console.WriteLine("Home was not able to complete"); }
        }
        public static void MoveStage(Brushless30XMotorChannel channel, Decimal position)
        {
            try
            {
                Console.WriteLine("Move started");
                channel.MoveTo(position, 60000);
            }
            catch (Exception)
            { Console.WriteLine("Move was not able to complete"); }
        }
        public static void JogStage(Brushless30XMotorChannel channel, MotorDirection direction)
        {
            try
            {
                channel.MoveJog(direction, 60000);
            }
            catch (Exception)
            { Console.WriteLine("Jog was not able to complete"); }
        }
    }
}
