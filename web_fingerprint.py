import urllib.request

target = "http://192.168.56.102"
print(f"Fingerprinting: {target}")
print("-" * 40)

try:
    response = urllib.request.urlopen(target)
    headers = response.info()
    print(f"Server: {headers['Server']}")
    print(f"Content-Type: {headers['Content-Type']}")
    print(f"Status Code: {response.status}")
except Exception as e:
    print(f"Error: {e}")

print("-" * 40)
print("Fingerprinting complete!")
