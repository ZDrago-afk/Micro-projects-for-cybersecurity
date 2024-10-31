import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in range(1, ports + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
target_ip = input("Enter the target IP address: ")
num_ports = int(input("Enter the number of ports to scan: "))
scan_ports(target_ip, num_ports)