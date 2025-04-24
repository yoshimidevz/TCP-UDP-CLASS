import socket

def start_server(addr: str, port: int):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((addr, port))

    print(f"UDP server listening on {addr}:{port}")

    while True:
        data, address= server_socket.recvfrom(1024)
        print(f'{address[1]}-Message: {data}')
        server_socket.sendto("Msg Recebida!".encode(),address)

if __name__=="__main__":
    HOST= 'localhost'
    PORT= 6000
    start_server(HOST,PORT)