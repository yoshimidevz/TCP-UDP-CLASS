import socket

def start_client(address: str, port: int):
    client_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input('Digite sua mensagem: ').encode()
        client_server.sendto(message,(address,port))
        data = client_server.recvfrom(1024)
        print(f'Mensagem direto do servidor: {data}')

if __name__=="__main__":
    HOST = 'localhost'
    PORT = 6000

    start_client(HOST,PORT)