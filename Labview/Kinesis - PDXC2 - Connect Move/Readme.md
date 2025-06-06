### Thorlabs Hardware: PDXC2 - Compact Single Stage ORIC Piezo Inertia Stage Controller  
https://www.thorlabs.com/thorproduct.cfm?partnumber=PDXC2  

# Description:  
This VI will enable you to communicate with PDXC2 series to control Piezo Inertia Stages. The VI will first connect and initialize the device, home the stage if the "Closed Loop" tab is enabled, and move the stage to a specified location.  

# Instructions:  
1) Connect your device to your PC & power the device. ensuring your stage is connected prior to powering the device. For full device setup, the device product manual can be found on our website.  
2) Enter the device serial number and the target position.  
3) If the stage is equipped with encoders (PDX1(/M), PDX1A(/M), PDX1AV(/M), PDX2(/M), PDX3(/M), PDX4(/M), PDXZ1(/M), PDXR1(/M)) and the 'Closed Loop' tab is enabled, ensure the device move path is clear for homing.  
4) Click 'Run' in the LabVIEW Toolbar which will attempt a connection. And a home command will be sent when the 'Closed Loop' tab is enabled.  
5) Wait for the device to be available, then the stage will move to the target position.   
