import socket

def send_message_to_server(addr: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((addr, port))
    message = 'ping'
    server_sendall(message.encode())

if _name_ == '_main_':
    HOST='localhost'
    PORT=8000

    send_message_to_server(HOST, PORT)