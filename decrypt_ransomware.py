from cryptography.fernet import Fernet
import os

# Read the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

print("[*] Decryption Started")

# Decrypt all files in test_folder
folder = os.path.expanduser("~/test_folder")
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        print(f"[+] Decrypting: {filename}")
        with open(filepath, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(filepath, "wb") as file:
            file.write(decrypted_data)

print("[!] All files decrypted!")
print("[!] Your files have been restored.")
