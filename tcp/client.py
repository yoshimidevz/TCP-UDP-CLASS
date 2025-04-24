import socket


def start_client(address: str,port: int):
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = input('Digite sua mensagem: ').encode()

    client_server.connect((address,port))
    client_server.sendall(message)
    data = client_server.recv(1024)
    print(f'Mensagem direto do servidor: {data.decode()}')

if __name__=="__main__":
    HOST = 'localhost'
    PORT = 8000

    start_client(HOST,PORT)