import socket

# We will scan 'google.com' or '127.0.0.1'. 
# Google is better for screenshots because it has Port 80 and 443 open.
target = "google.com" 
ports = [21, 22, 80, 443, 3306, 8080]

print(f"--- ONEIX : VAPT SCANNER ---")
print(f"Targeting: {target}")
print("-" * 40)

for port in ports:
    # Creating a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Wait 1 second for a response
    
    print(f"Checking Port {port}...", end=" ")
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(">> OPEN [VULNERABLE]")
    else:
        print(">> Closed")
    s.close()

print("-" * 40)
print("Scan Complete.")