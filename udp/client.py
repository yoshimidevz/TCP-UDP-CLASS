import socket
import threading

def receive_messages(sock):
    """Recebe mensagens do servidor"""
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f"\n{data.decode()}\n> ", end="")
        except:
            break

def start_client(host: str, port: int):
    """Inicia o cliente do chat"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Pede o nome do usuário
    username = input("Digite seu nome: ")
    client_socket.sendto(username.encode(), (host, port))  # Primeira mensagem é o nome
    
    # Inicia thread para receber mensagens
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    print(f"\nBem-vindo(a) ao chat, {username}! Digite suas mensagens abaixo:")
    while True:
        message = input('> ')
        client_socket.sendto(message.encode(), (host, port))

if __name__ == "__main__":
    print("=== CLIENTE DO CHAT UDP ===")
    start_client('localhost', 8000)