import time

__author__ = 'ankurkhandelwal'

import serial


s=serial.Serial(port='/bin',baudrate=9600, timeout=5)
time.sleep(2)
print(s)
running=0
while running:
    readData=s.readline()
    print(readData, "Arduino value")



data=raw_input("Select value")
if data=='1':
    s.write(data)
elif data=='0':
    s.write(data)
else:
    print("Invalid")

s.close()