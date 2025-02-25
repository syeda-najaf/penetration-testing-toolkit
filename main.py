import sys
import os

# Add the 'modules' directory to Python's import path
MODULES_DIR = os.path.join(os.path.dirname(__file__), "modules")
if MODULES_DIR not in sys.path:
    sys.path.append(MODULES_DIR)

# Import modules safely
try:
    from port_scanner import port_scan
    from brute_forcer import brute_force
except ModuleNotFoundError as e:
    print(f"❌ Error: {e}")
    print("Make sure the 'modules' folder exists and contains 'port_scanner.py' and 'brute_forcer.py'.")
    sys.exit(1)  # Exit with an error code
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Check if the module files have the correct functions and are not corrupted.")
    sys.exit(1)

def main():
    print("\n🔹 Penetration Testing Toolkit 🔹")
    print("1. Port Scanner")
    print("2. Brute-Force Attack")
    
    choice = input("\nChoose an option: ").strip()
    
    if choice == "1":
        target_ip = input("Enter target IP: ").strip()
        ports_input = input("Enter ports (comma-separated): ").strip()

        try:
            ports = list(map(int, ports_input.split(',')))
        except ValueError:
            print("❌ Error: Invalid port numbers.")
            return
        
        print(f"🔍 Scanning {target_ip} on ports {ports}...")
        port_scan(target_ip, ports)

    elif choice == "2":
        target_url = input("Enter login URL: ").strip()
        user = input("Enter username: ").strip()
        password_file = input("Enter password list file: ").strip()

        if not os.path.exists(password_file):
            print(f"❌ Error: The file '{password_file}' was not found.")
            return

        try:
            with open(password_file, 'r') as file:
                passwords = [line.strip() for line in file if line.strip()]

            if not passwords:
                print("❌ Error: Password file is empty.")
                return

            print(f"🔑 Attempting brute-force on {target_url} with user '{user}'...")
            brute_force(target_url, user, passwords)
        except Exception as e:
            print(f"❌ Error reading password file: {e}")

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
