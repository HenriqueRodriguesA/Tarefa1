import socket
HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hold = (HOST, PORT)
s.bind(hold)
s.listen()
print ('aguardando conexao com cliente')
con, ender = s.accept()
print ('Concetado por', ender)
while True:
    num = con.recv(1024)
    if not num:
        print ('Finalizando conexao do cliente', ender)
        s.close()
        break
    new_string = num[::-1]
    con.sendall(new_string)
