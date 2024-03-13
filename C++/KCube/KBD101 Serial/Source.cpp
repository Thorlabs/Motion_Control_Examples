//Example Date of Creation(YYYY-MM-DD): 2024-03-13
//Example Date of Last Modification on Github:  2024-03-13
//Version of C++ for Testing adn IDE:C++ 14, Visual Studio 2022
//Version of the ftd2xx.dll or ftd2xx64.dll used: 3.2.16.1
#include "stdlib.h"
#include "stdio.h"
#include "ftd2xx.h"

FT_HANDLE Initilize(char* HWSerialNum);
void Home(FT_HANDLE ftHandle);
void MoveTo(FT_HANDLE ftHandle, double position);
void SetMoveVelocity(FT_HANDLE ftHandle, double velocity, double acceleration);

//Stage Parameters. See page 39 of com protocol document
double pos_conversion = 2000; // Encorder Counts. This is stage dependant. 
double vel_conversion = 13421.77; // Scaling factor for velocity. This is stage dependant. 
double acc_conversion = 1.374; // Scaling factor for acceleration. This is stage dependant. 


int main()
{
	FT_HANDLE ftHandle;
	FT_STATUS ftStatus;
	DWORD numDevs;
	FT_DEVICE_LIST_INFO_NODE* devInfo=NULL;

	//Get the number of connected devices
	ftStatus = FT_CreateDeviceInfoList(&numDevs);
	// allocate storage for list based on numDevs
	devInfo = (FT_DEVICE_LIST_INFO_NODE*)malloc(sizeof(FT_DEVICE_LIST_INFO_NODE) * numDevs);
	//Get the device information list
	ftStatus = FT_GetDeviceInfoList(devInfo, &numDevs);
	//Displayed the devices
	if (numDevs == 0)
	{
		printf("No Device detected.");
		return 0;
	}
	for (unsigned int i = 0; i < numDevs; i++)
	{
		printf("Dev %d:\n", i+1);
		printf(" SerialNumber=%s\n", devInfo[i].SerialNumber);
		printf(" Description=%s\n", devInfo[i].Description);
	}

	//Select the device to connect
	unsigned int x = 0 ;
	printf("Select an instrument: ");
	scanf_s("%d",&x);
	if (x > numDevs || x == 0)
	{
		printf("invalid input!");
		return 0;
	}

	//Initilize the device
	ftHandle = Initilize(devInfo[x-1].SerialNumber);

	/*****************Do Stuff*******************/
	if (ftHandle != 0)
	{
		Home(ftHandle);
		SetMoveVelocity(ftHandle, 2, 4);
		MoveTo(ftHandle, 5);  

		// Close Device
		Sleep(1000);
		FT_Close(ftHandle);
	}
	return 1;
}


FT_HANDLE Initilize(char* HWSerialNum)
{
	DWORD BytesWritten;
	DWORD BytesReceived;
	DWORD RxBytes = 0;
	DWORD TxBytes;
	DWORD EventDWord;
	char RxBuffer[90];
	int count = 0;

	FT_HANDLE ftHandle;
	FT_OpenEx(HWSerialNum, FT_OPEN_BY_SERIAL_NUMBER, &ftHandle);
	// Set baud rate to 115200.
	FT_SetBaudRate(ftHandle, 115200);
	// 8 data bits, 1 stop bit, no parity
	FT_SetDataCharacteristics(ftHandle, FT_BITS_8, FT_STOP_BITS_1, FT_PARITY_NONE);
	// Pre purge dwell 50ms.
	Sleep(50);
	// Purge the device.
	FT_Purge(ftHandle, FT_PURGE_RX | FT_PURGE_TX);
	// Post purge dwell 50ms.
	Sleep(50);
	// Reset device.
	FT_ResetDevice(ftHandle);
	// Set flow control to RTS/CTS.
	FT_SetFlowControl(ftHandle, FT_FLOW_RTS_CTS, 0, 0);
	// Set RTS.
	FT_SetRts(ftHandle);
	// Set time out
	FT_SetTimeouts(ftHandle, 2000, 2000);

	//Notify the controller of the source and destination addresses || MGMSG_HW_NO_FLASH_PROGRAMMING || 0x0018
	char TxBuffer[] = { 0x18, 0x00, 0x00, 0x00, 0x50, 0x01 };
	FT_Write(ftHandle, TxBuffer, sizeof(TxBuffer), &BytesWritten);
	Sleep(100);

	//Request Hardware information || MGMSG_HW_REQ_INFO || 0x0005
	char TxBuffer1[] = { 0x05, 0x00, 0x00, 0x00, 0x50, 0x01 };
	FT_Write(ftHandle, TxBuffer1, sizeof(TxBuffer1), &BytesWritten);
	Sleep(100);

	//Get Hardware information || MGMSG_HW_GET_INFO || 0x0006
	//if the hardware info can't be get after 500000 times loop, it's considered that it fails to communicate.
	while (RxBytes < 90 && count < 50000)
	{
		FT_GetStatus(ftHandle, &RxBytes, &TxBytes, &EventDWord);
		count += 1;
	}
	if (count == 50000)
	{
		printf("Fail to communicate.\n");
		FT_Close(ftHandle);
		return 0;
	}
	FT_Read(ftHandle, RxBuffer, sizeof(RxBuffer), &BytesReceived);
	char serialNumBuffer[4] = { RxBuffer[6],RxBuffer[7],RxBuffer[8],RxBuffer[9]};

	//convert from byte to decimal
	int serialNum = 0;
	for (int i = 0; i < 4; i++)
	{
		serialNum |= static_cast<unsigned char>(serialNumBuffer[i]) << (i * 8);
	}
	printf("Connected to %d\n", serialNum);
	
	return ftHandle;
}

void Home(FT_HANDLE ftHandle)
{
	DWORD BytesWritten;
	DWORD BytesReceived;
	DWORD RxBytes = 0;
	DWORD TxBytes;
	DWORD EventDWord;

	//Clear the buffer and pending/current reads or writes
	FT_W32_PurgeComm(ftHandle, PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_TXABORT | PURGE_RXABORT);

	//Enable the channel || MGMSG_MOD_SET_CHANENABLESTATE || 0x0210
	char TxBuffer1[] = { 0x10, 0x02, 0x01, 0x01, 0x50, 0x01 }; 
	FT_Write(ftHandle, TxBuffer1, sizeof(TxBuffer1), &BytesWritten); 
	Sleep(100);

	//Home the stage || MGMSG_MOT_MOVE_HOME || 0x0443
	char TxBuffer2[] = { 0x43, 0x04, 0x01, 0x00, 0x50, 0x01 };
	FT_Write(ftHandle, TxBuffer2, sizeof(TxBuffer2), &BytesWritten); 
	printf("\nHoming the stage.");
	Sleep(100);


	//Get Status Update Message
	char RxBuffer[20];
	char ifHomed = 0;
	int count = 0;
	char TxBuffer3[] = { 0x90, 0x04, 0x01, 0x00, 0x50, 0x01 };
	while (ifHomed != 4)
	{
		//Clear the buffer and pending/current reads or writes
		FT_W32_PurgeComm(ftHandle, PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_TXABORT | PURGE_RXABORT);

		Sleep(100);
		//Request Status Update Message || MGMSG_MOT_REQ_USTATUSUPDATE || 0x0490
		FT_Write(ftHandle, TxBuffer3, sizeof(TxBuffer3), &BytesWritten);
		//Get Status Update Message || MGMSG_MOT_GET_USTATUSUPDATE || 0x0491
		while (RxBytes < 20) FT_GetStatus(ftHandle, &RxBytes, &TxBytes, &EventDWord);
		FT_Read(ftHandle, RxBuffer, sizeof(RxBuffer), &BytesReceived);

		//the meaning of the RxBuffer[17]:
		//0x01 = connected, 0x02 = homing, 0x04 homed
		//0x40 = position error
		ifHomed = RxBuffer[17] & 0b00001111; // only judge the lower 4 bits

		//if the stage still hasn't homed after 150 times loop, it's considered that it fails to home.
		if (count > 150)
		{
			printf("The stage fails to home.\n\n");
			break;
		}
		count += 1;

	}
	if (ifHomed == 4)  printf("The stage is homed.\n\n");
}

void MoveTo(FT_HANDLE ftHandle, double position)
{
	DWORD BytesWritten;
	DWORD BytesReceived;
	DWORD TxBytes;
	DWORD EventDWord;
	DWORD RxBytes = 0;

	//Clear the buffer and pending/current reads or writes
	FT_W32_PurgeComm(ftHandle, PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_TXABORT | PURGE_RXABORT);

	unsigned int encoder_pos = position * pos_conversion;

	//Convert from deciaml to byte
	char epb[4]; //encoder postion in bytes
	unsigned char ch;
	for (int i = 0; i < 4; i++)
	{
		ch = (encoder_pos >> ((i & 7) << 3)) & 0xFF;
		epb[i] = ch;
	}

	//Absolute Move || MGMSG_MOT_MOVE_ABSOLUTE || 0x0453
	char TxBuffer1[] = {0x53, 0x04, 0x06, 0x00, 0xD0, 0x01, 0x01, 0x00, epb[0], epb[1], epb[2], epb[3]};
	FT_Write(ftHandle, TxBuffer1, sizeof(TxBuffer1), &BytesWritten);
	printf("The stage is moving to %f mm\n", position);
	Sleep(100);

	//Get Status Update Message
	char RxBuffer[20];
	char ifMoving = 1;
	char TxBuffer2[6] = { 0x90, 0x04, 0x01, 0x00, 0x50, 0x01 };

	while (ifMoving != 0)
	{
		//Clear the buffer and pending/current reads or writes
		FT_W32_PurgeComm(ftHandle, PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_TXABORT | PURGE_RXABORT);

		Sleep(100);
		//Request Status Update Message || MGMSG_MOT_REQ_USTATUSUPDATE || 0x0490
		FT_Write(ftHandle, TxBuffer2, sizeof(TxBuffer2), &BytesWritten);

		//Get Status Update Message || MGMSG_MOT_GET_USTATUSUPDATE || 0x0491
		while (RxBytes < 20) FT_GetStatus(ftHandle, &RxBytes, &TxBytes, &EventDWord);
		FT_Read(ftHandle, RxBuffer, sizeof(RxBuffer), &BytesReceived);
		
		//the meaning of the RxBuffer[16]:
		//0x01=hardware limit clockwise, 0x02=hardware limit counter clockwise
		//0x10=in motion clockwise, 0x20=in motion counter clcokwise
		//0x40=jogging clockwise, 0x80=jogging counter clockwise, 
		ifMoving = (RxBuffer[16] >> 4);	//only judge the higher 4 bits
	}

	//get the current position. 
	//Wait 1 second to accomplish the stage close-loop adjustment
	Sleep(1000);

	//Request Status Update Message || MGMSG_MOT_REQ_USTATUSUPDATE || 0x0490
	FT_Write(ftHandle, TxBuffer2, sizeof(TxBuffer2), &BytesWritten);
	//Get Status Update Message || MGMSG_MOT_GET_USTATUSUPDATE || 0x0491
	while (RxBytes < 20) FT_GetStatus(ftHandle, &RxBytes, &TxBytes, &EventDWord);
	FT_Read(ftHandle, RxBuffer, sizeof(RxBuffer), &BytesReceived);

	char posBuffer[4] = { RxBuffer[8],RxBuffer[9],RxBuffer[10],RxBuffer[11] };

	//convert from byte to decimal
	int encoder_posGet = 0;
	for (int i = 0; i < 4; i++)
	{
		encoder_posGet |= static_cast<unsigned char>(posBuffer[i]) << (i * 8);
	}

	//convert the unit to the real world unit
	double posGet = encoder_posGet / pos_conversion;
	printf("The stage stops at %f mm\n", posGet);
}

void SetMoveVelocity(FT_HANDLE ftHandle, double velocity, double acceleration)
{
	DWORD BytesWritten;
	DWORD BytesReceived;
	DWORD EventDWord;

	//Clear the buffer and pending/current reads or writes
	FT_W32_PurgeComm(ftHandle, PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_TXABORT | PURGE_RXABORT);

	int encoder_vel = velocity * vel_conversion;
	int encoder_acc = acceleration * acc_conversion;

	//Convert from deciaml to byte
	char evb[4]; //encoder velocity in bytes
	char eab[4]; //encoder acceleration in bytes
	unsigned char ch;
	for (int i = 0; i < 4; i++)
	{
		ch = (encoder_vel >> ((i & 7) << 3)) & 0xFF;
		evb[i] = ch;
		ch = (encoder_acc >> ((i & 7) << 3)) & 0xFF;
		eab[i] = ch;
	}
	//Set Velocity Parameters ||MGMSG_MOT_SET_VELPARAMS || 0x0413
	char TxBuffer[] = { 0x13, 0x04, 0x0E, 0x00, 0xD0, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, eab[0], eab[1], eab[2], eab[3], evb[0], evb[1], evb[2], evb[3] };
	FT_Write(ftHandle, TxBuffer, sizeof(TxBuffer), &BytesWritten);
	Sleep(100);
}



