import socket

def broadcast_message(server_sock, sender_name, message, sender_addr, recipients):
    """Envia mensagem para todos os clientes conectados exceto o remetente"""
    for client_addr in recipients:
        if client_addr != sender_addr:
            formatted_msg = f"{sender_name}: {message}"
            server_sock.sendto(formatted_msg.encode(), client_addr)

def handle_clients(server_sock):
    """Gerencia o conjunto de clientes conectados"""
    connected_clients = {}  # Agora armazena {endereço: nome}
    
    while True:
        try:
            msg_data, client_addr = server_sock.recvfrom(1024)
            message = msg_data.decode()
            
            # Se é um novo cliente, a primeira mensagem é o nome
            if client_addr not in connected_clients:
                connected_clients[client_addr] = message
                print(f"{message} entrou no chat!")
                broadcast_message(server_sock, "Servidor", f"{message} entrou no chat!", client_addr, connected_clients.keys())
            else:
                print(f"{connected_clients[client_addr]}: {message}")
                broadcast_message(server_sock, connected_clients[client_addr], message, client_addr, connected_clients.keys())
                
        except Exception as e:
            print(f"Erro: {e}")
            break

def start_server(host: str, port: int):
    """Inicia o servidor UDP"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))
    
    print(f"Servidor de chat iniciado em {host}:{port}")
    print("Aguardando participantes...\n")
    
    handle_clients(udp_socket)

if __name__ == '__main__':
    start_server('localhost', 8000)