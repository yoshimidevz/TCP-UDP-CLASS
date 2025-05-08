import socket
import threading

def listen_messages(sock):
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f'\n[Received message]: {data.decode()}\nType your message:', end=' ')
        except:
            break

def start_client(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    
    threading.Thread(target=listen_messages, args=(client_socket,), daemon=True).start()
    
    while True:
        message = input('Type your message: ')
        client_socket.sendto(message.encode(), (host, port))

def send_message(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.settimeout(1)

    while True:
        message = input('Type your message:')
        server.sendto(message.encode(), (host, port))

        data, addr = server.recvfrom(1024)
        print(f'[Message]: {data.decode()}')

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8000

    start_client(HOST, PORT)