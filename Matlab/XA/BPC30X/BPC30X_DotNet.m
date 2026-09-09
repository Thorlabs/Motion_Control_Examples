% Title: BPC30X
% Modification Date: 09/09/2026
% Example Description:
% This example demonstrates how to connect to a BPC30X device and channel,
% zero it, set the maximum output voltage, and output a voltage.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*
import Thorlabs.MotionControl.XA.Piezo.*

% Change this line to match the serial number on your device.
deviceId = '1234';
% Select the channel to control ("1", "2", or "3").
channelNumber = '1';

% Start up XA.
systemManager = SystemManager.Create();
systemManager.Startup();

% Get the device list.
devicelist = systemManager.GetDeviceList();
if isempty(devicelist)
    fprintf('Connected devices: %d\n', 0);
else
    fprintf('Connected devices: %d\n', devicelist.Count);
end
if ~isempty(devicelist) && devicelist.Count > 0
    index = 1;
    for k = 1:devicelist.Count
        d = devicelist.Item(k-1);
        fprintf('Device %d: ', index);
        try
            fprintf('%s, Serial Number: %s\n', char(d.DeviceType.ToString()), char(d.Device));
        catch
            if ~isempty(d)
                fprintf('%s\n', char(d.ToString()));
            else
                fprintf('<null device>\n');
            end
        end
        index = index + 1;
    end
else
    fprintf('No devices found.\n');
end

% Open the BPC30X base device.
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('\nFail to open base unit %s\n', deviceId);
    systemManager.Shutdown();
    return;
end
fprintf('\nBase Unit %s opened successfully\n', deviceId);

% Open the channel.
channelId = [deviceId '-' channelNumber];
[ret, channel] = systemManager.TryOpenDevice(channelId, '', OperatingModes.Default);
if ~ret
    fprintf('Fail to open channel %s\n', channelId);
    device.Close();
    systemManager.Shutdown();
    return;
end
fprintf('Channel %s opened successfully\n', char(channel.DeviceId));

try
    % Enable the channel.
    channel.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(60));
    fprintf('Channel enabled successfully.\n');

    % Zero the piezo channel.
    channel.SetZero(System.TimeSpan.FromSeconds(60));
    fprintf('Voltage zeroed successfully.\n');

    % Set the maximum output voltage.
    maxOutputVoltage = int16(25);
    channel.SetMaxOutputVoltage(maxOutputVoltage);
    fprintf('Maximum output set successfully.\n');
    System.Threading.Thread.Sleep(200);

    % Get the maximum output voltage.
    voltageParams = channel.GetMaxOutputVoltageParams(System.TimeSpan.FromSeconds(60));
    fprintf('New maximum output voltage is: %d\n', voltageParams.MaxOutputVoltage);

    % Set the output voltage.
    outputVoltage = int16(10);
    channel.SetOutputVoltage(outputVoltage);
    fprintf('Output voltage set successfully.\n');
    System.Threading.Thread.Sleep(200);

    % Get the output voltage.
    readbackVoltage = channel.GetOutputVoltage(System.TimeSpan.FromSeconds(60));
    fprintf('New output voltage is: %d\n', readbackVoltage);

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the channel.
if ~isempty(channel)
    channel.Close();
end
% Close the device.
if ~isempty(device)
    device.Disconnect();
    device.Close();
end
fprintf('Channel closed.\n');
% Shutdown XA.
systemManager.Shutdown();
