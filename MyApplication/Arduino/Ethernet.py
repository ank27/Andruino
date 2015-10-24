__author__ = 'ankurkhandelwal'

from socket import *
import time
import serial

# here the server is arduino so we give address of server
# check the ip address of arduino in arduino_python_over_ethernet

server_address=('192.168.1.125', 8888)  #ip+port

# socket is object which will send packet data
# AF_INET is an address family that is used to designate the type of addresses
# that your socket can communicate with (in this case, Internet Protocol v4 addresses).
#
# SOCK_DGRAM is for datagram communication
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  #this will ensure that if arduino doesnt respond our program wont crash,

#now talk
while 1 : #this means forever
    data="Blue"
    client_socket.sendto(data,server_address)
    try:
        #read response from arduino
        received_data, addr=client_socket.recvfrom(2048) #just size as big int, addr is address of client which alredy defined server_address
        print(received_data)
    except:
        pass #just pass and go for next loop

    time.sleep(2)

    data="Red"
    client_socket.sendto(data,server_address)
    try:
        received_data, addr=client_socket.recvfrom(2048)
        print(received_data)
    except:
        pass

    time.sleep(2)





##################################################
def send_temp_pressure():
    while 1:
        data="temprature"
        client_socket.sendto(data,server_address)
        try:
            received_data,addr=client_socket.recvfrom(2048)
            print(received_data)
        except:
            pass
        time.sleep(2)

        data="pressure"
        client_socket.sendto(data,server_address)
        try:
            received_data,addr=client_socket.recvfrom(2048)
            print(received_data)
        except:
            pass
        time.sleep(2)