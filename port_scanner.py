import socket

def port_scan(target, ports):
    target = target.strip()  # Remove extra spaces
    print(f"\n🔎 Scanning {target} on ports: {ports}")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")

            sock.close()
        except Exception as e:
            print(f"❌ Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ").strip()
    ports = list(map(int, input("Enter ports (comma-separated): ").split(',')))

    port_scan(target_ip, ports)
