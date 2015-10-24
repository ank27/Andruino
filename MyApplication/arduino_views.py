from django.http import request
import time

__author__ = 'ankurkhandelwal'
import django
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render
import serial
from django.http import HttpResponse
from socket import *


port="/dev/tty.usbmodem1421"
baud_rate=9600

server_address=('192.168.1.125', 8888)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  #this will ensure that if arduino doesnt respond our program wont crash,


@django.views.decorators.csrf.csrf_exempt
def send_binary_values(request):
    return render(request,'minovate/form-common.html')


@django.views.decorators.csrf.csrf_exempt
def send_data(request):
    x=request.GET.get('led_state',"")
    try:
        s=serial.Serial(port=port,baudrate=baud_rate, timeout=5)
        time.sleep(2)
        binary_value='0'
        if(x=="true"):
            binary_value='1'
            print("True",binary_value)
            s.write(binary_value)
        elif(x=="false"):
            print("False",binary_value)
            s.write(binary_value)
            time.sleep(0.1)
        else:
            print("Invalid!!")
    except:
        print("Not connected!!")



################===================Ethernet Connection==========================
@django.views.decorators.csrf.csrf_exempt
def send_temp_data(request):
    if request.POST:
        temprature=request.POST.get("temprature_data")
        ir=request.POST.get("IR_Sensor")
        light=request.POST.get("photo_sensor")
        client_socket.settimeout(1)
        client_socket.sendto(temprature,server_address)
        try:
            recieved_data=client_socket.recvfrom(2048)
            print("temprature ",recieved_data)
        except:
            pass
        time.sleep(1)

        client_socket.sendto(ir,server_address)
        try:
            recieved_data=client_socket.recvfrom(2048)
            print("ir_sensor ",recieved_data)
        except:
            pass
        time.sleep(1)

        client_socket.sendto(light,server_address)
        try:
            recieved_data=client_socket.recvfrom(2048)
            print(" light_sensor", recieved_data)
        except:
            pass
#==================================================================================

#  //////////////////////////////  app data /////////////////
@django.views.decorators.csrf.csrf_exempt
def app_data(request):
    x=request.POST.get("led_state")
    print(x)
    s=serial.Serial(port=port,baudrate=baud_rate, timeout=5)
    time.sleep(2)
    binary_value='0'
    if(x=="true"):
        binary_value='1'
        print("True",binary_value)
        s.write(binary_value)
        return HttpResponse("200",content_type='application/json')
    elif(x=="false"):
        print("False",binary_value)
        s.write(binary_value)
        return HttpResponse("200",content_type='application/json')
    else:
        print("Invalid!!")
        return HttpResponse("401",content_type='application/json')