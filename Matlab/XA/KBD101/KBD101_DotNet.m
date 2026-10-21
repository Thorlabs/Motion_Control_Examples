% Title: KBD101
% Modification Date: 09/09/2026
% Example Description:
% This example demonstrates how to connect to a KBD101 device, home it,
% and perform an absolute move of 5 mm.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*

% Change this line to match the serial number on your device.
deviceId = '1234';

% Start up XA.
systemManager = SystemManager.Create();
systemManager.Startup();

% Open the KBD101 device.
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('Failed to open device %s\n', deviceId);
    systemManager.Shutdown();
    return;
end
fprintf('Device %s opened successfully\n', deviceId);

try
    % Enable the device.
    device.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(60));
    fprintf('Device enabled successfully.\n');

    % Get the hardware information.
    hardwareInfo = device.GetHardwareInfo(System.TimeSpan.FromSeconds(1));
    fprintf('Device Name: %s\n', char(hardwareInfo.PartNumber));

    % Home the device.
    fprintf('Homing...\n');
    device.Home(System.TimeSpan.FromSeconds(60));
    fprintf('Homed successfully.\n');

    % Distance to move.
    distance = 5.0;

    % Get the unit type from the connected actuator.
    productInfo = device.GetConnectedProductInfo();
    deviceUnit = productInfo.UnitType;

    % Convert the physical distance to device units.
    valueInDeviceUnits = device.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
    fprintf('Conversion from %g mm successful. Value in device units: %d\n', distance, valueInDeviceUnits);

    % Absolute move to 5 mm.
    fprintf('Moving to %g %s\n', distance, char(deviceUnit.ToString()));
    device.Move(MoveMode.Absolute, int32(valueInDeviceUnits), System.TimeSpan.FromSeconds(60));
    fprintf('Absolute move successful.\n');

    % Get the current position.
    currentPosInDeviceUnits = device.GetPositionCounter(System.TimeSpan.FromSeconds(60));
    currentPos = device.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
    fprintf('Current Position: %g %s\n', currentPos.Value, char(currentPos.UnitType.ToString()));

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the device.
device.Disconnect();
device.Close();
fprintf('Device closed.\n');
% Shutdown XA.
systemManager.Shutdown();
