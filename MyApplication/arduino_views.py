from django.http import request
import time
import simplejson
from MyApplication.models import UserProfile
from gcm import GCM
import django
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render
import serial
from django.http import HttpResponse
from socket import *
from MyApplication.constant import *

port='/dev/tty.usbmodem1411/'
baud_rate=9600

server_address=('52.89.219.153', 80)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  #this will ensure that if arduino doesnt respond our program wont crash,

@django.views.decorators.csrf.csrf_exempt
# ====read data from Arduino======
def read_data():
    s=serial.Serial(port=port,baudrate=baud_rate, timeout=5)
    time.sleep(2)
    while True:
        req=s.readline()
        if req:
            print(req)



@django.views.decorators.csrf.csrf_exempt
def send_binary_values(request):
    f = open('MyApplication/workfile.txt','r+')
    data=f.read()
    aray=data.split(',')
    f.close()
    context={
        'temprature':aray[0],
        'light_intensity':aray[1],
        'motion_value':aray[2],
        'light1':aray[3],
        'light2':aray[4],
        'light3':aray[5],
        'light4':aray[6],
    }
    return render(request,'minovate/index.html',context)


# ======================send data from web to arduino==================
@django.views.decorators.csrf.csrf_exempt
def send_data(request):
    light1_state=request.GET.get("light1","")
    light2_state=request.GET.get("light2","")
    light3_state=request.GET.get("light3","")
    light4_state=request.GET.get("light4","")
    temp=request.GET.get("temp","")
    light_intensity=request.GET.get("light_intensity","")
    motion=request.GET.get("motion","")
    # print(temp+","+light_intensity+","+motion)
    send_str=light1_state +","+light2_state+","+light3_state+","+light4_state
    f=open('MyApplication/workfile.txt','r+')
    final_str=temp+","+light_intensity+","+motion+","+send_str
    f.write(final_str)
    f.close()
    print(final_str)
    try:
        s=serial.Serial(port=port,baudrate=baud_rate, timeout=10)
        time.sleep(2)
        s.write(final_str.encode('utf-8'))
        time.sleep(1)
        return render(request,'minovate/index.html')
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
            # print("temprature ",recieved_data)
        except:
            pass
        time.sleep(1)

        client_socket.sendto(ir,server_address)
        try:
            recieved_data=client_socket.recvfrom(2048)
            # print("ir_sensor ",recieved_data)
        except:
            pass
        time.sleep(1)

        client_socket.sendto(light,server_address)
        try:
            recieved_data=client_socket.recvfrom(2048)
            # print("light_sensor ", recieved_data)
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


# ---================-=================final code from app(send and get data=============================================================
# Temprature
# Light intensity
# Motion
#4 led's == 4 bulb
# Get and Post for all the event.....get Temp, light, motion, led states
# and Post 1)to get all values  2)to change led states
@django.views.decorators.csrf.csrf_exempt
def send_app_data(request):
    f = open('MyApplication/workfile.txt','r+')
    data=f.read()
    data_dict={}
    led_aray=[]
    aray=data.split(',')
    f.close()
    data_dict["temp"]=aray[0]
    data_dict["light_intensity"]=aray[1]
    data_dict["motion_value"]=aray[2]
    led_aray.append({"light1":aray[3],"light2":aray[4],"light3":aray[5],"light4":aray[6]})
    data_dict["led_state"]=led_aray
    serial_json=simplejson.dumps(data_dict)
    # print(serial_json)
    return HttpResponse(serial_json, content_type='application/json')


@django.views.decorators.csrf.csrf_exempt
def get_app_data(request):
    light=request.POST.get("light","")
    state=request.POST.get("state","")
    f=open('MyApplication/workfile.txt','r')
    data=f.read()
    aray=data.split(',')
    f.close()
    if(light=='1'):
        aray[3]=state
    elif(light=='2'):
        aray[4]=state
    elif(light=='3'):
        aray[5]=state
    elif(light=='4'):
        aray[6]=state

    final_str=aray[0]+","+aray[1]+","+aray[2]+","+aray[3]+","+aray[4]+","+aray[5]+","+aray[6]
    fw=open('MyApplication/workfile.txt','w')
    fw.write(final_str)
    fw.close()
    # print(final_str)
    return HttpResponse("200",content_type='application/json')


def send_notification(app_id):
    api_key="AIzaSyBzAFQ19gB3BctG6VL8lO85VWf8I-vD_Gs"
    gcm=GCM(api_key)
    data = {'title':'Notify','extra': "Welcome to Arduino"}
    print(data)
    response = gcm.json_request(registration_ids=[app_id], data=data)
    return response


@django.views.decorators.csrf.csrf_exempt
def register_app_id(request):
    if request.POST:
        email=str(request.POST.get("email",""))
        app_id=str(request.POST.get("app_id",""))
        device_id=str(request.POST.get("device_id",""))
        app_version=str(request.POST.get("app_version",""))
        print("register_app"," ",email," ",app_id ," ",device_id," ",app_version)
        try:
            if(email):
                UserProfile(email=email,app_id=app_id,device_id=device_id,app_version=app_version).save()
                send_notification(app_id)
                print("app_id",app_id)
            else:
                print("User not present")
        except Exception as e:
            print(e.message)
        return HttpResponse("200",content_type='application/json')
    else:
        return HttpResponse("401",content_type='application/json')
