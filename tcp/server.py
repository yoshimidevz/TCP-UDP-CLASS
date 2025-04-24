import socket

HOST = 'localhost'
PORT = 8000

def start_server(address: str,port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen(1)

    print("Servidor rodando...")
    while True:
        client, address = server_socket.accept()
        print(f'Conexão aceita no end. {address}')
        data = client.recv(1024)
        print(f'Messagem: {data.decode()}')
        client.send('Mensagem recebida !'.encode())
        client.close()

if __name__=="__main__":
    start_server(HOST,PORT)