# run this entire code in the Anaconda command prompt.
# 1. type python 
# 2. type import server as server 
# 2. type import client as client
# 3. Simultaneously on other device, run the client file and establish the connection by entering the IP address of the server.
# 4. Now, enter the filename with extension i.e. the file which you want to transfer to the client.
# 5. Now, in the client side, enter the name which you want it to be saved as with the same extension.


# The Server File
import socket
import time

name =  "network.csv"
delay = 1

def run():
   print ("Starting " + name)
   while 1:
       time.sleep(delay)
       print ("%s: %s" % (name, time.ctime(time.time())))
       sending_file(name)
   print ("Exiting " + name)

def sending_file(filename):
    s= socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print("Waiting for any incoming connections ...")
    conn, addr = s.accept()
    print(addr, "Has connected to the server")
    
    #filename = input(str("Please enter the filename of the file: "))
    file = open(filename, 'rb')
    file_data = file.read(4096*4096)
    #file_data = file.read(19327352832)
    conn.send(file_data)
    print("Data has been transmitted successfully")
    
    
run()

# The Client File

import socket
import time

ip = '192.168.1.227'
delay = 1
name = "network22.csv"

def run_client():
    print('starting')
    while 1:
        time.sleep(delay)
        print("%s: %s" %(ip, time.ctime(time.time())))
        reciving_file(ip)
        
def reciving_file(ip):
    s = socket.socket()
    port = 8080
    s.connect((ip,port))
    print("Connected ... ")
    
    file = open(name, 'wb')
    file_data = s.recv(4096*4096)
    #file_data = s.recv(19327352832)
    file.write(file_data)
    file.close()
    print("File has been received successfully.")


run_client()
