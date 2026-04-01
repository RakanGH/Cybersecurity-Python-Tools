import socket
import time

# --- SETUP ---
target = input("Enter target to scan (e.g., google.com): ")

print(f"\n🚀 Starting Full Scan on {target}...")
print("Checking ports 1 to 1024. Please wait...\n")

start_scan = time.time()
open_ports = []

# --- SCANNING LOOP ---
for port in range(1, 1025):
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # We set a VERY short timeout (0.1s) to speed things up
    s.settimeout(0.1)

    # connect_ex returns 0 if successful
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port:4}: ✅ OPEN")
        open_ports.append(port)

    s.close()

end_scan = time.time()

# --- RESULTS ---
print("\n" + "=" * 30)
print(f"Scan Finished in {end_scan - start_scan:.2f} seconds")
print(f"Total Open Ports: {len(open_ports)}")
if open_ports:
    print(f"Open List: {open_ports}")
print("=" * 30)