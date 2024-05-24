import socket
import ipaddress
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        elif result == 10035:
            print(f"Port {port} is close")
        sock.close()
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}")

def scan_subnet(subnet, ports):
    try:
        ip_net = ipaddress.ip_network(subnet)
        for ip in ip_net.hosts():
            for port in ports:
                print(ip)
                thread = threading.Thread(target=scan_port, args=(str(ip), port))
                thread.start()
    except ValueError as e:
        print(f"Invalid subnet: {e}")

def get_input():
    subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")
    ports_input = input("Enter the ports to scan (comma-separated, e.g., 22,80,443): ")
    ports = [int(port.strip()) for port in ports_input.split(',')]
    return subnet, ports

def main():
    subnet, ports = get_input()
    scan_subnet(subnet, ports)

if _name_ == "_main_":
    main()