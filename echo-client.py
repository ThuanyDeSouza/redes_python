import socket

server = '127.0.0.1' # endereço do servidor ao qual vamos conectar
port = 12345 # porta à qual vamos conectar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #abre socket TCP
    sock.connect((server, port))
    sock.sendall(b'Hello World!')
    data = sock.recv(1024)
    
print('Recebido', repr(data))

