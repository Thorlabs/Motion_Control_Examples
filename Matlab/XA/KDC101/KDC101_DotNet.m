% Title: KDC101
% Modification Date: 08/24/2026
% Example Description:
% This example demonstrates how to set-up the communication for the Thorlabs
% KDC101 controllers, home it, and move it by 1 mm or degrees.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*

% Change this line to match the serial number on your device
deviceId = '27268055';

% Start up XA
systemManager = SystemManager.Create();
systemManager.Startup();

% Open the device (C# 'out' parameter becomes an extra return value)
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('Fail to open device %s\n', deviceId);
    systemManager.Shutdown();
    return;
end
fprintf('Device %s opened successfully\n', deviceId);

try
    % Enable the device
    device.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(1));

    % Get hardware information
    hardwareInfo = device.GetHardwareInfo(System.TimeSpan.FromSeconds(1));
    fprintf('Device Name: %s\n', char(hardwareInfo.PartNumber));

    % Home device
    fprintf('Homing\n');
    device.Home(System.TimeSpan.FromSeconds(60));
    fprintf('Homing completed\n');

    % Set the distance
    distance = 1;

    % Get the unit type of the actuator
    productInfo = device.GetConnectedProductInfo();
    deviceUnit  = productInfo.UnitType;

    % Distance to device unit
    valueInDeviceUnits = device.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);

    % Move device
    fprintf('Moving to %g %s\n', distance, char(deviceUnit.ToString()));
    device.Move(MoveMode.RelativeMove, int32(valueInDeviceUnits), System.TimeSpan.FromSeconds(60));
    fprintf('Moving completed\n');

    % Get the current position
    currentPosInDeviceUnits = device.GetPositionCounter(System.TimeSpan.FromSeconds(1));

    % Device unit to distance
    currentPos = device.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
    fprintf('Current Position: %g %s\n', currentPos.Value, char(currentPos.UnitType.ToString()));

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the device and shutdown XA
device.Disconnect();
device.Close();
systemManager.Shutdown();
