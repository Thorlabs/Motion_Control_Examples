"""
PDXC2 Ctypes Example
Date of Creation(YYYY-MM-DD): 2024-02-01
Date of Last Modification on Github: 2024-02-01
Python Version Used: python 3.10.5
Kinesis Version Tested: 1.14.45

"""


import os
import time
import sys
import numpy as np
from enum import Enum
import ctypes
from ctypes import *

#Load DLL file  
KinesisDir = r"C:\Program Files\Thorlabs\Kinesis" #("C:\Program Files (x86)\Thorlabs\Kinesis" for 32-bit software)
DllFile    = "Thorlabs.MotionControl.Benchtop.Piezo.dll"
if sys.version_info < (3, 8):
    os.chdir(KinesisDir) 
else:
    os.add_dll_directory(KinesisDir)
lib = cdll.LoadLibrary(DllFile)
lib.TLI_InitializeSimulations()     
 
#Device Serial Number 
SerialNum = c_char_p(b"112000001")  

#Position Pointer
Position = c_int(1)
PositionPointer = pointer(Position)

# Positon Control Mode
class ControlMode(Enum):
    # Open Loop
    PZ_OpenLoop = 1
    # Close loop
    PZ_CloseLoop = 2

class PZ_AmpOutMode(Enum):
	BothDirections = c_int16(1)
	OneOutputPerDirection = c_int16(2)

    
class MOT_TravelDirection(Enum):
	MOT_TravelDirectionDisabled = 0
	MOT_Forwards = 1
	MOT_Reverse = 2

class PZ_JogModes(Enum):
    # Open Loop
    JogContinuous = 1
    # Close loop
    JogStep = 2


class PDXC2_JogParameters(Structure):
    _fields_ = [
	("JogMode"                                , c_int16        ),# 
	("OpenLoopStepSize_Low16bit"              , c_int16        ),#
    ("OpenLoopStepSize_High16bit"             , c_int16        ),#
	("OpenLoopStepRate_Low16bit"              , c_int16        ),#
    ("OpenLoopStepRate_High16bit"             , c_int16        ),#
	("OpenLoopAcceleration_Low16bit"          , c_int16        ),#
    ("OpenLoopAcceleration_High16bit"         , c_int16        ),#
	("ClosedLoopStepSize_Low16bit"            , c_int16        ),#
    ("ClosedLoopStepSize_High16bit"           , c_int16        ),#
	("ClosedLoopSpeed_Low16bit"               , c_int16        ),#
    ("ClosedLoopSpeed_High16bit"              , c_int16        ),#
	("ClosedLoopAcceleration_Low16bit"        , c_int16        ),#
    ("ClosedLoopAcceleration_High16bit"       , c_int16        ),
    ] 
   
    
class PZ_AmpOutParameters(Structure):
    _fields_ = [
	("AmpOutMode"                             , c_int16        ),# No used, Reserved.
	("ForwardAmplitude"                       , c_int16        ),# 
    ("ReverseAmplitude"                       , c_int16        ),#
    ] 


class PDXC2_OpenLoopMoveParameters(Structure):
    _fields_ = [
    ("StepSize"       , c_int32        ) ,
    ("Reserved1"      , c_int32        ) ,
    ("Reserved2"      , c_int32        ) ,
    ] 

   

class PDXC2_ClosedLoopParameters(Structure):
    _fields_ = [
            ("RefSpeed"      , c_uint32  ),
            ("Proportional"  , c_uint32  ),
            ("Integral"      , c_uint32  ),
            ("Differential"  , c_uint32  ),
            ("Acceleration"  , c_uint32  ),          
            ]

def EnableDevice(serialnum):
    if lib.TLI_BuildDeviceList() == 0:
        ret = lib.PDXC2_Open(serialnum)
        print(f'PDXC2_Open Returned {ret}') 
        if(ret == 0):
            lib.PDXC2_Enable(serialnum)
            print('Device Enabled') 
            return(0)
        else :
            print('No Device Detected')
            return(1)
    else :
        print('No Device Detected') 
        return(1)

#Set the Move mode to closed loop mode
def Set2ClosedLoopMode(serialnum):
    CtrlMode = ControlMode.PZ_CloseLoop.value
    lib.PDXC2_SetPositionControlMode(serialnum ,CtrlMode)   
    print("Set the operation mode to closed loop mode")
    
#Set the Move mode to closed loop mode
def Set2OpenLoopMode(serialnum):
    CtrlMode = ControlMode.PZ_OpenLoop.value
    lib.PDXC2_SetPositionControlMode(serialnum ,CtrlMode)   
    print("Set the operation mode to open loop mode")    
    
#Get the Position(nm) for closed loop mode / Steps Counter for open loop mode 
def GetPosition(serialnum):
    lib.PDXC2_RequestPosition(serialnum)
    lib.PDXC2_GetPosition(serialnum,PositionPointer)   
    return(Position.value)

#Open loop set move control
def OpenLoopSetMove(serialnum , steps ):    
    OpenLoopMoveParams = [steps, c_int32(0) , c_int32(0) ]   
    OpenLoopParamSet = PDXC2_OpenLoopMoveParameters(*OpenLoopMoveParams) 
    lib.PDXC2_SetOpenLoopMoveParams(serialnum , OpenLoopParamSet) 
    lib.PDXC2_MoveStart(serialnum)    

#Set the Open loop set move Step Rate / acceleration , Set Move and Jog use the same set of these parameters
def OpenLoopSetMoveParamsSet(serialnum , steprate ,acceleration ) :
    PDXC2_GetJogParams = lib.PDXC2_GetJogParams
    PDXC2_GetJogParams.argtypes = [ctypes.c_char_p, ctypes.POINTER(PDXC2_JogParameters)]
    PDXC2_GetJogParams.restype = ctypes.c_int
    ParamsGet = PDXC2_JogParameters()
    lib.PDXC2_RequestJogParams(serialnum)
    result = PDXC2_GetJogParams(SerialNum, ctypes.byref(ParamsGet))
    
    JogMode                          =  ParamsGet.JogMode         
    OpenLoopStepSize_Low16bit        =  ParamsGet.OpenLoopStepSize_Low16bit 
    OpenLoopStepSize_High16bit       =  ParamsGet.OpenLoopStepSize_High16bit
    OpenLoopStepRate_Low16bit        =  steprate & 0xFFFF      
    OpenLoopStepRate_High16bit       =  (steprate>>16) & 0xFFFF   
    OpenLoopAcceleration_Low16bit    =  acceleration & 0xFFFF      
    OpenLoopAcceleration_High16bit   =  (acceleration>>16) & 0xFFFF   
    ClosedLoopStepSize_Low16bit      =  ParamsGet.ClosedLoopStepSize_Low16bit  
    ClosedLoopStepSize_High16bit     =  ParamsGet.ClosedLoopStepSize_High16bit 
    ClosedLoopSpeed_Low16bit         =  ParamsGet.ClosedLoopSpeed_Low16bit      
    ClosedLoopSpeed_High16bit        =  ParamsGet.ClosedLoopSpeed_High16bit
    ClosedLoopAcceleration_Low16bit  =  ParamsGet.ClosedLoopAcceleration_Low16bit  
    ClosedLoopAcceleration_High16bit =  ParamsGet.ClosedLoopAcceleration_High16bit
    
    ParamsSet               =     PDXC2_JogParameters (JogMode                        ,             
                                                      OpenLoopStepSize_Low16bit       ,
                                                      OpenLoopStepSize_High16bit      ,
                                                      OpenLoopStepRate_Low16bit       ,
                                                      OpenLoopStepRate_High16bit      ,
                                                      OpenLoopAcceleration_Low16bit   ,
                                                      OpenLoopAcceleration_High16bit  ,
                                                      ClosedLoopStepSize_Low16bit     ,
                                                      ClosedLoopStepSize_High16bit    ,
                                                      ClosedLoopSpeed_Low16bit        ,
                                                      ClosedLoopSpeed_High16bit       ,
                                                      ClosedLoopAcceleration_Low16bit ,
                                                      ClosedLoopAcceleration_High16bit, )
                                                      
    lib.PDXC2_SetJogParams(serialnum , ctypes.byref(ParamsSet))
    

def OpenLoopJogMoveParamsSet(serialnum ,jogmode , stepsize , steprate ,acceleration ) :
    PDXC2_GetJogParams = lib.PDXC2_GetJogParams
    PDXC2_GetJogParams.argtypes = [ctypes.c_char_p, ctypes.POINTER(PDXC2_JogParameters)]
    PDXC2_GetJogParams.restype = ctypes.c_int
    ParamsGet = PDXC2_JogParameters()
    lib.PDXC2_RequestJogParams(serialnum)
    result = PDXC2_GetJogParams(SerialNum, ctypes.byref(ParamsGet))
    
    JogMode                          =  jogmode         
    OpenLoopStepSize_Low16bit        =  stepsize & 0xFFFF      
    OpenLoopStepSize_High16bit       =  (stepsize>>16) & 0xFFFF
    OpenLoopStepRate_Low16bit        =  steprate & 0xFFFF      
    OpenLoopStepRate_High16bit       =  (steprate>>16) & 0xFFFF   
    OpenLoopAcceleration_Low16bit    =  acceleration & 0xFFFF      
    OpenLoopAcceleration_High16bit   =  (acceleration>>16) & 0xFFFF   
    ClosedLoopStepSize_Low16bit      =  ParamsGet.ClosedLoopStepSize_Low16bit  
    ClosedLoopStepSize_High16bit     =  ParamsGet.ClosedLoopStepSize_High16bit 
    ClosedLoopSpeed_Low16bit         =  ParamsGet.ClosedLoopSpeed_Low16bit      
    ClosedLoopSpeed_High16bit        =  ParamsGet.ClosedLoopSpeed_High16bit
    ClosedLoopAcceleration_Low16bit  =  ParamsGet.ClosedLoopAcceleration_Low16bit  
    ClosedLoopAcceleration_High16bit =  ParamsGet.ClosedLoopAcceleration_High16bit
    
    ParamsSet               =     PDXC2_JogParameters (JogMode                        ,             
                                                      OpenLoopStepSize_Low16bit       ,
                                                      OpenLoopStepSize_High16bit      ,
                                                      OpenLoopStepRate_Low16bit       ,
                                                      OpenLoopStepRate_High16bit      ,
                                                      OpenLoopAcceleration_Low16bit   ,
                                                      OpenLoopAcceleration_High16bit  ,
                                                      ClosedLoopStepSize_Low16bit     ,
                                                      ClosedLoopStepSize_High16bit    ,
                                                      ClosedLoopSpeed_Low16bit        ,
                                                      ClosedLoopSpeed_High16bit       ,
                                                      ClosedLoopAcceleration_Low16bit ,
                                                      ClosedLoopAcceleration_High16bit, )
                                                      
    lib.PDXC2_SetJogParams(serialnum , ctypes.byref(ParamsSet))

    
def ClosedLoopJogMoveParamsSet(serialnum ,jogmode , stepsize , speed , acceleration ) :
    PDXC2_GetJogParams = lib.PDXC2_GetJogParams
    PDXC2_GetJogParams.argtypes = [ctypes.c_char_p, ctypes.POINTER(PDXC2_JogParameters)]
    PDXC2_GetJogParams.restype = ctypes.c_int
    ParamsGet = PDXC2_JogParameters()
    lib.PDXC2_RequestJogParams(serialnum)
    result = PDXC2_GetJogParams(SerialNum, ctypes.byref(ParamsGet))
    
    JogMode                          =  jogmode         
    OpenLoopStepSize_Low16bit        =  ParamsGet.OpenLoopStepSize_Low16bit     
    OpenLoopStepSize_High16bit       =  ParamsGet.OpenLoopStepSize_High16bit   
    OpenLoopStepRate_Low16bit        =  ParamsGet.OpenLoopStepRate_Low16bit     
    OpenLoopStepRate_High16bit       =  ParamsGet.OpenLoopStepRate_High16bit    
    OpenLoopAcceleration_Low16bit    =  ParamsGet.OpenLoopAcceleration_Low16bit 
    OpenLoopAcceleration_High16bit   =  ParamsGet.OpenLoopAcceleration_High16bit 
    ClosedLoopStepSize_Low16bit      =  stepsize & 0xFFFF      
    ClosedLoopStepSize_High16bit     =  (stepsize>>16) & 0xFFFF
    ClosedLoopSpeed_Low16bit         =  speed & 0xFFFF      
    ClosedLoopSpeed_High16bit        =  (speed>>16) & 0xFFFF   
    ClosedLoopAcceleration_Low16bit  =  acceleration & 0xFFFF       
    ClosedLoopAcceleration_High16bit =  (acceleration>>16) & 0xFFFF 
    
    ParamsSet               =     PDXC2_JogParameters (JogMode                        ,             
                                                      OpenLoopStepSize_Low16bit       ,
                                                      OpenLoopStepSize_High16bit      ,
                                                      OpenLoopStepRate_Low16bit       ,
                                                      OpenLoopStepRate_High16bit      ,
                                                      OpenLoopAcceleration_Low16bit   ,
                                                      OpenLoopAcceleration_High16bit  ,
                                                      ClosedLoopStepSize_Low16bit     ,
                                                      ClosedLoopStepSize_High16bit    ,
                                                      ClosedLoopSpeed_Low16bit        ,
                                                      ClosedLoopSpeed_High16bit       ,
                                                      ClosedLoopAcceleration_Low16bit ,
                                                      ClosedLoopAcceleration_High16bit, )
                                                      
    lib.PDXC2_SetJogParams(serialnum , ctypes.byref(ParamsSet))    
 
def AdjustAmp(serialnum , forwardamp , reverseamp):
    AdjustAmpParams = [c_int16(0) , c_int16(forwardamp) , c_int16(reverseamp) ]   
    AdjustAmpParamSet = PZ_AmpOutParameters(*AdjustAmpParams) 
    lib.PDXC2_SetAmpOutParams(serialnum , AdjustAmpParamSet) 

#Set the closed loop set move parameters(PID & speed & acceleration)
def ClosedLoopSetMoveParamsSet(serialnum , refspeed ,proportional , integral ,differential , acceleration ) :
    ClosedLoopMoveParams = [c_uint32(refspeed) , c_uint32(proportional) , c_uint32(integral) , c_uint32(differential) ,c_uint32(acceleration)]
    ClosedLoopMoveParamsSet = PDXC2_ClosedLoopParameters(*ClosedLoopMoveParams)
    lib.PDXC2_SetClosedLoopParams(serialnum , ClosedLoopMoveParamsSet)
    
#Home or Zero Operaiton
#When in closed loop mode, This operation will drive the stage to Zero position
#When in open loop mode, This operation will not drive the stage, Only Zero the counter of steps.
def Home(serial_num):
    print("Start Home/Zero Operation ")
    PosCheckCnt = 0 
    lib.PDXC2_Home(serial_num)
    for i in range(0,100):
        lib.PDXC2_RequestPosition(serial_num)
        lib.PDXC2_GetPosition(serial_num,PositionPointer)
        if(abs(Position.value - 0) < 6000 ):
            if(PosCheckCnt > 3 ):  
                time.sleep(0.5)              
                break ;
            else :       
                time.sleep(0.5)             
                PosCheckCnt = PosCheckCnt + 1      
        else :       
            time.sleep(0.5)             
    print("Home/Zero Operation Finished")

if __name__ == '__main__':
    ErrFlag = EnableDevice(SerialNum)
    if(ErrFlag == 0):
        ####################################################################################
        ## Close Loop Set Move Control Example
        #################################################################################### 
        #Set operation mode to closed loop mode
        Set2ClosedLoopMode(SerialNum)
        time.sleep(1)
        #Home operation
        Home(SerialNum)  
        time.sleep(1)
        
        #Set the RefSpeed to 10mm/s, Proportional to 8192 , Integral to 8192 , Differential to 0 , Acceleration to 50mm/s^2
        ClosedLoopSetMoveParamsSet(SerialNum , 10000000 , 8192 , 8192 , 0 , 50000000 )
        
        #Set target position to 5mm 
        print("Set target position to 5mm")        
        lib.PDXC2_SetClosedLoopTarget(SerialNum ,c_int(5000000))
        lib.PDXC2_MoveStart(SerialNum)   
        time.sleep(3)
        
        #Set target position to -5mm
        print("Set target position to -5mm")  
        lib.PDXC2_SetClosedLoopTarget(SerialNum ,c_int(-5000000))
        lib.PDXC2_MoveStart(SerialNum)          
        time.sleep(3)
        
        ####################################################################################
        ## Close Loop Jog Move Control Example
        ####################################################################################         
        #-------------------Single Step Move-----------------# 
        
        #Set Closed Loop Jog Move step size 3mm , speed to 5mm/s  , and config the acceleration to 50mm/s^2
        ClosedLoopJogMoveParamsSet(SerialNum ,PZ_JogModes.JogStep.value , 3000000 , 5000000 ,50000000 ) ;
        print("Set Closed Loop Jog Move step size 1mm , speed to 5mm/s  , and config the acceleration to 50mm/s^2")
        
        #Sigle forward step move
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Forwards.value)
        print("Signle Step Jog Forward Move Start")
        time.sleep(2)
        print("Signle Step Jog Forward Move End")
        
        #Sigle reverse step move
        print("Signle Step Jog Reverse Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Reverse.value)
        time.sleep(2)   
        print("Signle Step Jog Reverse Move End")
        
        #-------------------Continuous Step Move-----------------# 
        #Set Closed Loop Jog Move step size 3mm , speed to 1mm/s  , and config the acceleration to 50mm/s^2
        ClosedLoopJogMoveParamsSet(SerialNum ,PZ_JogModes.JogContinuous.value , 3000000 , 1000000 ,50000000 ) ; 
        print("Set Closed Loop Jog Move step size 3mm , speed to 10mm/s  , and config the acceleration to 50mm/s^2")
        
        #Continuous forward step move
        print("Continuous Jog Forward Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Forwards.value)  
        time.sleep(3)
        
        #Move Stop Control
        print("Continuous Jog Forward Move Stop")
        lib.PDXC2_MoveStop(SerialNum)
        time.sleep(3)
        
        #Continuous reverse step move
        print("Continuous Jog Reverse Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Reverse.value)
        time.sleep(3)        

        #Move Stop Control
        print("Continuous Jog Reverse Move Stop")
        lib.PDXC2_MoveStop(SerialNum)
        time.sleep(3)
        
        
        
        ###################################################################################
        # Open Loop Set Move Control Example
        ###################################################################################
        #Set operation mode to open loop 
        Set2OpenLoopMode(SerialNum)
        time.sleep(1)

        #Home operation
        Home(SerialNum)  
        time.sleep(1)
        
        #Set Open Loop Set Move step rate to 20K step/s , and config the acceleration to 20K steps/s^2         
        OpenLoopSetMoveParamsSet(SerialNum , 20000 ,20000 )

        #Get Steps Counter
        StepCounter = GetPosition(SerialNum)
        print("Current Step Counter is ",StepCounter)
        
        #Set Move forward 20K steps
        print("Set Move forward 20K steps")
        OpenLoopSetMove(SerialNum , StepCounter + 20000) 
        time.sleep(2)    
        
        #Move reverse 20K steps back to StepCounter
        print("Move reverse 20K steps back to StepCounter")
        OpenLoopSetMove(SerialNum , StepCounter ) 
        time.sleep(2)              

        
        ###################################################################################
        # Open Loop Jog Move Control Example
        ###################################################################################
        
        #-------------------Single Step Move-----------------# 
        
        #Set Open Loop Jog Move step size 2k, step rate to 2K step/s , and config the acceleration to 20K steps/s^2 
        OpenLoopJogMoveParamsSet(SerialNum ,PZ_JogModes.JogStep.value , 2000 , 2000 ,20000 ) ;
        print("Set Open Loop Jog Move step size 2k, step rate to 2K step/s , and config the acceleration to 20K steps/s^2")
        
        #Sigle forward step move
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Forwards.value)
        print("Signle Step Jog Forward Move Start")
        time.sleep(2)
        print("Signle Step Jog Forward Move End")
        
        #Sigle reverse step move
        print("Signle Step Jog Reverse Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Reverse.value)
        time.sleep(2)   
        print("Signle Step Jog Reverse Move End")
        
        #-------------------Continuous Step Move-----------------# 
        #Set Open Loop Jog Move step size 2k, step rate to 2K step/s , and config the acceleration to 20K steps/s^2 
        OpenLoopJogMoveParamsSet(SerialNum ,PZ_JogModes.JogContinuous.value , 2000 , 2000 ,20000 ) ; 
        print("Set Open Loop Jog Move step size 2k, step rate to 2K step/s , and config the acceleration to 20K steps/s^2")
        
        #Continuous forward step move
        print("Continuous Jog Forward Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Forwards.value)  
        time.sleep(2)
        
        #Move Stop Control
        print("Continuous Jog Forward Move Stop")
        lib.PDXC2_MoveStop(SerialNum)
        time.sleep(1)
        
        #Continuous reverse step move
        print("Continuous Jog Reverse Move Start")
        lib.PDXC2_MoveJog(SerialNum, MOT_TravelDirection.MOT_Reverse.value)
        time.sleep(2)        

        #Move Stop Control
        print("Continuous Jog Reverse Move Stop")
        lib.PDXC2_MoveStop(SerialNum)
        time.sleep(1)

        ###################################################################################
        # Adjust amplitude test example
        ###################################################################################
        #Adjust forward and reverse amplitude to 50% voltage output
        print("Adjust forward and reverse amplitude to 50% voltage output")
        AdjustAmp(SerialNum , 50 , 50 ) 
        
        #Get Steps Counter
        StepCounter = GetPosition(SerialNum)
        print("Current Step Counter is ",StepCounter)
        
        #Set Move forward 20K steps
        print("Set Move forward 20K steps")
        OpenLoopSetMove(SerialNum , StepCounter + 20000) 
        time.sleep(2)    
        
        #Move reverse 20K steps back to StepCounter
        print("Move reverse 20K steps back to StepCounter")
        OpenLoopSetMove(SerialNum , StepCounter ) 
        time.sleep(2)
        
        #Disconnect the device
        lib.PDXC2_Close(SerialNum)      
        
        
        
        
        