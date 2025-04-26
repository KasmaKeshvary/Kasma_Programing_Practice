import socket

def listen_on_port(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
        server_socket.listen(1)
        print(f"Listening on port {port}...")
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        conn.close()
        server_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    port = 51250
    listen_on_port(port)