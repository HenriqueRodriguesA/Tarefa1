import socket
HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hold = (HOST, PORT)
s.connect(hold)
num = input('Digite um numero:')
num = hex(an_interger)
print('valor em hexadecimal:', num)
