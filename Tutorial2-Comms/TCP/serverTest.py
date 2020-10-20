
import socket

s = socket.socket()
host = socket.gethostname()  #ip of raspberry pi
port = 8080
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  from_client = ''
  print ('Got connection from',addr)
  while True:
    data = c.recv(4096)
    if not data: break
    #from_client += data
    print(data)
    c.send('I am SERVER'.encode())
  c.close()
  print("Client disconnected")

