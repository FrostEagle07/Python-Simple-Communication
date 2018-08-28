import socket    
import sys  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

while True:

  TCP_IP = input("Server adress : ")
  TCP_PORT = input("Server port : ")  
  TCP_PORT = int(TCP_PORT)
  print("")           

  print('Connecting to ', TCP_IP, TCP_PORT)
  print("")
  print("--------------------------->")
  s.connect((TCP_IP, TCP_PORT))

  try:
    while True:
      msg = input('CLIENT >> ').encode()
      s.send(msg)
      msg = s.recv(1024)
      print('SERVER >>', msg.decode())

  except:
    accept = 0
    print("")
    print("Connexion lost")
    
    while accept == 0:
      losthandle = input("Print N for a new connexion | S to end current instance : ")
      if losthandle != "N" and losthandle != "S":
        print("<-- invalid input -->")
      else:
        accept = 1

  if losthandle == "S":
    sys.exit()

