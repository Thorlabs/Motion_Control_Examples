// Title: BBD30X_Raster_Scan
// Created Date: 04/19/2024
// Last Modified Date: 04/19/2024
// .NET Framework version: 4.8.2
// Thorlabs DLL version: 1.14.47
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// BBD Benchtop controllers and initiate a raster scan.




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
                Console.WriteLine("List fialed to build");
                return;
            }

            //Get the first available BBD300 controller
            //Check if there was a found device. If not, close the program
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
                //Initialize the controller
                controller.Connect(serialNumbers[0]);
                controller.GetMotherboardConfiguration(serialNumbers[0], DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);

                //Initialize the channels
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

                    //Set the movement parameters for the scan
                    xAxis.SetJogVelocityParams(200, 1000);
                    xAxis.SetVelocityParams(200, 1000);

                    yAxis.SetJogVelocityParams(200, 1000);
                    yAxis.SetVelocityParams(200, 1000);

                    //Scan parameters
                    Decimal startX = 25;
                    Decimal startY = 50;

                    Decimal endX = 75;
                    Decimal endy = 25;

                    int numberOfXPoints = 8;
                    int numberOfRows = 4;

                    xAxis.SetJogStepSize(Math.Abs(endX - startX) / numberOfXPoints);
                    yAxis.SetJogStepSize(Math.Abs(endy - startY) / numberOfRows);

                    //determine the direction the scan will be going for the x and y axes
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

                    //start the scan
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
                //close the controller connection
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
