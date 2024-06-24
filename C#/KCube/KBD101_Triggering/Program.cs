// Title: KBD101_Triggering
// Created Date: 02/11/2022
// Last Modified Date: 07/18/2023
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KBD101 controllers and how to set the triggers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.KCube.BrushlessMotorCLI;


namespace KBD101_Triggering
{
    class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line if you are using simulations
            // Also uncomment UnitializeSimulations() at the end of the file
            //SimulationManager.Instance.InitializeSimulations();

            try
            {
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception)
            {
                Console.WriteLine("Device list failed to build");
                return;
            }

            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubeBrushlessMotor.DevicePrefix);

            if (serialNumbers.Count > 0)
            {
                Console.WriteLine(serialNumbers[0]);
            }
            else
            {
                Console.WriteLine("No connected devices");
                return;
            }

            KCubeBrushlessMotor controller = KCubeBrushlessMotor.CreateKCubeBrushlessMotor(serialNumbers[0]);

            if (controller != null)
            {
                controller.Connect(serialNumbers[0]);
                controller.WaitForSettingsInitialized(3000);
                controller.LoadMotorConfiguration(controller.DeviceID);
                controller.SetSettings(controller.MotorDeviceSettings, true);

                controller.StartPolling(200);
                System.Threading.Thread.Sleep(500);
                controller.EnableDevice();
                System.Threading.Thread.Sleep(500);

                Console.WriteLine("Stage homing...");
                controller.Home(60000);
                Console.WriteLine("Homing finsihed");

                //Adjust settings for IO 1 and 2
                //Sets Trig Port 1 as input and 2 as output
                //Cube will output a high signal when in motion
                controller.SetTriggerConfigParams(new KCubeTriggerConfigParams()
                {
                    Trigger1Mode = KCubeTriggerConfigSettings.TriggerPortMode.TrigIN_RelativeMove,
                    Trigger2Mode = KCubeTriggerConfigSettings.TriggerPortMode.TrigOUT_InMotion,

                    Trigger1Polarity = KCubeTriggerConfigSettings.TriggerPolarity.TriggerHigh, 
                    Trigger2Polarity = KCubeTriggerConfigSettings.TriggerPolarity.TriggerHigh
                });

                //Set Move settings for the trigger in
                controller.SetVelocityParams(10m, 10m);
                controller.SetMoveRelativeDistance(10m);

                //Loop to allow triggers to come in
                Console.WriteLine("Type \"stop\" to end program");
                while (!Console.ReadLine().Contains("stop"))
                {
                    System.Threading.Thread.Sleep(100);
                }

                Console.WriteLine("Closing ...");
                controller.StopPolling();
                controller.DisableDevice();
            }

            // Uncomment this line if you are using a simulated device
            //SimulationManager.Instance.UninitializeSimulations();
        }
    }
}
