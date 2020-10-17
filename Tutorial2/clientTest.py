
import socket               

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
host = socket.gethostname() # ip of raspberry pi 
port = 8080              
client.connect((host, port))
client.send('I am CLIENT'.encode())
from_server = client.recv(4096)
print(from_server)
client.close()
print(from_server)


"""
import socket               

s = socket.socket()        
host = ''# ip of raspberry pi 
port = 8080               
s.connect((host, port))
print(s.recv(1024).decode())
s.close()
"""
