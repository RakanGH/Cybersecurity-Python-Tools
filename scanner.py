import socket
import datetime

target = "127.0.0.1"

print(f"Scanning target: {target}")

t1 = datetime.datetime.now()
# Loop from port 1 to 1024
for port in range(1, 1025):
    # Create the 'plug'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)  # 0.1 is fast! Total scan will take ~100 seconds.

    # Try the connection
    result = s.connect_ex((target, port))

    # --- YOUR LOGIC START ---
    # Check if result is 0
    # If it is, print: f"Port {port} is OPEN"
    # --- YOUR LOGIC END ---
    if port % 100 == 0: print(f"Checking port {port}...")
    if result == 0: print(f"Port {port} is open")

    # Close the plug so we can use a new one in the next loop
    s.close()

t2 = datetime.datetime.now()
total = t2 - t1
print(f"Scanning completed in: {total}")