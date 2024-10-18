
'''

import socket
import threading
import queue

host = "103.181.69.19"
q = queue,queue()

for i in range(1,1001):
    q.put(i)

def scan():
    while not q.empty():
        port = q.get()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    s.connect((host,port ))
    print(f'prot {port} is open!')

except :
    pass
q.task_done()


for i in range (30):
    t = threading.Thread(target=scan, doemon = True)
    t = start()


q.join()
print('finished')

'''

import socket
import threading
import queue

host = "103.181.69.19"  # লক্ষ্য সার্ভারের আইপি
q = queue.Queue()  # কাজের জন্য একটি কিউ

# 1 থেকে 10000 পোর্টের তালিকা কিউতে যোগ করা
for i in range(1, 10001):
    q.put()

def scan():
    while not q.empty():
        port = q.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP পোর্ট স্ক্যানিংয়ের জন্য SOCK_STREAM ব্যবহার করা হচ্ছে
        try:
            s.connect((host, port))
            print(f'Port {port} is open!')
        except:
            pass  # যদি কোনো পোর্ট বন্ধ থাকে, তাহলে কিছু করবে না
        finally:
            s.close()
            q.task_done()  # কাজ সম্পূর্ণ হলে কিউতে জানিয়ে দেয়

# ৩০টি থ্রেড তৈরি করা হবে যা পোর্ট স্ক্যান করবে
for i in range(30):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

q.join()  # সমস্ত কাজ শেষ না হওয়া পর্যন্ত অপেক্ষা করা
print('Finished scanning')



