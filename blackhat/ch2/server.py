import socket

# Membuat socket tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# meng-set host dan port server 
s.bind((socket.gethostname(), 1234))

# enable server for accpt connection. Hanya bisa 5 koneksi dalam satu waktu 
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been establish.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
