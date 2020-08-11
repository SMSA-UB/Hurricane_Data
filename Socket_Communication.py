# run this entire code in the Anaconda command prompt.
# 1. type python 
# 2. type import server as server 
# 2. type import client as client
# 3. Simultaneously on other device, run the client file and establish the connection by entering the IP address of the server.
# 4. Now, enter the filename with extension i.e. the file which you want to transfer to the client.
# 5. Now, in the client side, enter the name which you want it to be saved as with the same extension.



# The Server File
import socket

s= socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for any incoming connections ...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str("Please enter the filename of the file: "))
file = open(filename, 'rb')
file_data = file.read(19327352832)
conn.send(file_data)
print("Data has been transmitted successfully")


# The Client file
import socket
s = socket.socket()
host = input(str("Please enter the host address of the sender : " ))
port = 8080
s.connect((host,port))
print("Connected ... ")

filename = input(str("Please enter a filename for the incoming file : "))
file = open(filename, 'wb')
file_data = s.recv(19327352832)
file.write(file_data)
file.close()
print("File has been received successfully.")