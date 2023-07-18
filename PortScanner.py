import socket
import time

MIN_PORT = 1
MAX_PORT = 65535
SCAN_DELAY = 0.1

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...")
    
    if start_port < MIN_PORT or end_port > MAX_PORT:
        print(f"Invalid port range. Port numbers should be between {MIN_PORT} and {MAX_PORT}")
        return
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except socket.error:
            print(f"Error occurred while scanning port {port}")
        time.sleep(SCAN_DELAY)

target_host = input("Enter the target host: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

scan_ports(target_host, start_port, end_port)
