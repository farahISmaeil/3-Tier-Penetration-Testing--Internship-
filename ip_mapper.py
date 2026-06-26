import socket

target = "192.168.56.102"
print(f"IP Mapping for: {target}")
print("-" * 40)

# Hostname lookup
try:
    hostname = socket.gethostbyaddr(target)
    print(f"Hostname: {hostname[0]}")
except:
    print("Hostname: Not found")

# Open ports check
print("\nChecking common ports:")
common_ports = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 21: "FTP"}
for port, service in common_ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"  Port {port} ({service}): OPEN")
    sock.close()

print("-" * 40)
print("Mapping complete!")
