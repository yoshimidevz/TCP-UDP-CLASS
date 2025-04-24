import socket

def start_server(addr   , port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((addr, port))
    server_socket.listen(1)

    print(f 'Server está rodando.. addr: {addr} port: {port}')

    while True:
        client_socket, addr= server_socket.accept()
        print(f'Conexão estabelecida com {addr} na porta {port}')

        data = client_socket.recv(1024).decode()

        if data == 'ping':
            client_socket.send('pong'.encode())
            
        print(f'[CLIENTE]: {data}')

        client_socket.close()


if _name_=='_main_':
    HOST = 'localhost'
    PORT = 8000

    start_server(HOST, PORT)