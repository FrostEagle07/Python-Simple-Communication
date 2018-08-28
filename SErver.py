import socket

print("SERVER CONFIG")
port = input("Port on which establish socket : ")
print("Server Adress : " + socket.gethostbyname(socket.gethostname()))
port = int(port)
print("<-------------------------------------")
print("")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
host = socket.gethostbyname(socket.gethostname())
s.bind((host, port)) 

print('SERVER STARTED')
print("------------------------------------->")
print("")

while True:  
  print('Waiting for connection...')    
  s.listen(5)                 
  c, addr = s.accept()     
  print('Connection received from', addr)
  print("")
  
  try:
    while True:
      msg = c.recv(1024)
      print("CLIENT >>", msg.decode())
      msg = input('SERVER >> ').encode()
      c.send(msg)
  
  except:
    pass
  
  print("")
  print('Connection lost from ', addr)
  print("")

  
