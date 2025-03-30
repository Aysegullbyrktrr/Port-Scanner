import socket
import ipaddress
import argparse
import logging
import time
from concurrent.futures import ThreadPoolExecutor

__version__ = "1.1.0"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DEFAULT_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389, 8080, 8443]

scan_results = {}

def scan_port(ip, port, detailed=False, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                banner = "N/A"
                if detailed:
                    try:
                        banner = sock.recv(1024).decode(errors="ignore").strip()
                    except Exception:
                        pass

                scan_results.setdefault(ip, []).append((port, banner))
    except Exception as e:
        logging.error(f"Error scanning {ip}:{port} - {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Professional Port Scanner Tool")
    parser.add_argument("subnet", help="Subnet or IP to scan (e.g., 192.168.1.0/24 or 192.168.1.1)")
    parser.add_argument("-p", "--ports", help="Ports to scan (comma-separated, e.g., 22,80,443). Defaults to common ports if omitted.", default=None)
    parser.add_argument("-d", "--detailed", action="store_true", help="Enable detailed scan (banner grabbing)")
    parser.add_argument("-T", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("-t", "--timeout", type=int, default=1, help="Socket timeout in seconds (default: 1)")
    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        network = ipaddress.ip_network(args.subnet, strict=False)
    except ValueError as e:
        logging.error(f"Invalid subnet: {e}")
        return

    ports = [int(port.strip()) for port in args.ports.split(',')] if args.ports else DEFAULT_PORTS
    host_list = list(network.hosts())

    logging.info(f"Starting scan on {args.subnet} using {'detailed' if args.detailed else 'fast'} mode...")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [
            executor.submit(scan_port, str(ip), port, args.detailed, args.timeout)
            for ip in host_list
            for port in ports
        ]
        for future in futures:
            future.result()

    scan_duration = time.time() - start_time

    print("\n--- SCAN RESULTS ---")
    if scan_results:
        for ip, ports in scan_results.items():
            print(f"\nHost: {ip} (Online)")
            for port, banner in sorted(ports):
                print(f"  - {port:<5}/tcp  OPEN  {banner}")
    else:
        print("No open ports found.")

    print(f"\nScan completed in {scan_duration:.2f} seconds.")

if __name__ == "__main__":
    main()
