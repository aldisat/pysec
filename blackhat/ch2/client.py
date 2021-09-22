import socket

# Membuat socket tcp 
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengkoneksikan socket dengan host dan port server tertentu
# gethostname == mengambill current host
s.connect((socket.gethostname(), 1234))

# berfungsi untuk menentukan berapa jumlah huruf yang akan diterima client
msg = s.recv(1024)

# menampilkan pesan
print(msg.decode("utf-8"))
