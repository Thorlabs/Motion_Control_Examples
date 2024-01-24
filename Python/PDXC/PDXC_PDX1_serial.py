import time 
import os, io, sys, re, time, json, base64
import datetime
import socket
import glob
import os 
import binascii
import serial
import serial.tools.list_ports
import time
import shutil
from decimal import Decimal

today = datetime.date.today()

WORK_FILE =  os.path.realpath(__file__)  
WORK_PATH =  os.path.dirname(os.path.abspath(__file__)) 

def SerialInit(port_serial):
    print("USE COM Number is",port_serial) 
    return(serial.Serial(port_serial, 115200))

def Ascii_to_Hex(ascii_str):
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str

def Hex_to_Ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str

def Home(COM):
    #convert the command to bytes value type
    op_string = ['H','O','M','=','1'] 
    for i in range(0,len(op_string)):
        op_string[i] = Ascii_to_Hex(op_string[i])
        op_string[i] = int(op_string[i],16)   
    transfer_dat = []
    for i in range(0,len(op_string)+1):
        if(i == len(op_string) ):
            transfer_dat.append(int('0d',16))
        else :
            transfer_dat.append(op_string[i])      
    cmd_bytes = bytes(transfer_dat)
    #write the home command
    COM.write(cmd_bytes)
    
def SpeedSet(COM,speed):
    op_string = ['s','p','d','=']   
    for i in range(0,len(speed)):
        op_string.append(speed[i])  
    #convert the command to bytes value type
    for i in range(0,len(op_string)):
        op_string[i] = Ascii_to_Hex(op_string[i])
        op_string[i] = int(op_string[i],16)   
    transfer_dat = []
    for i in range(0,len(op_string)+1):
        if(i == len(op_string) ):
            transfer_dat.append(int('0d',16))
        else :
            transfer_dat.append(op_string[i])      
    cmd_bytes = bytes(transfer_dat)
    #write the speed set command
    COM.write(cmd_bytes)    

def PosSet(COM,Pos):
    op_string = ['P','O','S','=']   
    for i in range(0,len(Pos)):
        op_string.append(Pos[i])
    #convert the command to bytes value type
    for i in range(0,len(op_string)):
        op_string[i] = Ascii_to_Hex(op_string[i])
        op_string[i] = int(op_string[i],16)   
    transfer_dat = []
    for i in range(0,len(op_string)+1):
        if(i == len(op_string) ):
            transfer_dat.append(int('0d',16))
        else :
            transfer_dat.append(op_string[i])      
    cmd_bytes = bytes(transfer_dat)
    #write the position set command
    COM.write(cmd_bytes)
    
def main():
    list_temp = []
    a = input('Serial Port：')
    a = "COM"+ a
    COM = SerialInit(a)
    b = input('Type the Target Postion_0(mm):')
    c = input('Type the Target Postion_1(mm):')
    d = input('Type the Speed(mm/s):')
    f = input('Total running time(s):')
    e = input('Cycle period(ms):')
    
    print("Start Home Operation")
    time.sleep(1)
    Home(COM)
    time.sleep(1)
    SpeedSet(COM,d)        
    time.sleep(5)   
    print("Start Cycle Test")
    
    f = int(f) #total running time
    e = int(e) #period
    m = int(f*1000/e) #total running count
    n = (e/2000) #wait time
    data = COM.read(COM.in_waiting) 
    list_temp.clear()

    for i in range(0,m):
        print("Cycle Running Count:",i)
        PosSet(COM,b)                 
        time.sleep(n) 
        PosSet(COM,c)        
        time.sleep(n)
    
if __name__ == '__main__':
    main()
