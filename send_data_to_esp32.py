import serial
import time

ser = serial.Serial("COM4", 115200)
time.sleep(2)

ser.write(b"hey")
ser.close()
