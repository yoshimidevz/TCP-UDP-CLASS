import socket

def start_server(addr: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((addr,port))
    server_socket.listen(1)

    print(f'Server está rodando..  addr: {addr} port: {port}')


    client_socket, addr= server_socket.accept()
    print(f'Conexão estabelecida no endereço: {addr}')

    while True:
        data = client_socket.recv(1024).decode()
        print(f'[CLIENTE]: {data}')

        client_socket.sendall('pong'.encode())

    # client_socket.close()



if __name__=='__main__':
    HOST='localhost'
    PORT=8000

    start_server(HOST, PORT)
