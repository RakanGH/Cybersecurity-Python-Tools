import os

current_directory = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_directory, "server_logs.txt")

print("[*] Starting Log Analysis...")

# 1. Initialize our counter at 0
critical_count = 0

try:
    with open(log_file, "r") as file:
        for line in file:
            if "CRITICAL" in line:
                print(f"[🚨 ALERT] Found critical event: {line.strip()}")
                # 2. Increment the counter by 1 whenever we find a match
                critical_count += 1

    # 3. Print the final summary report after finishing the loop
    print("\n" + "=" * 30)
    print("--- ANALYSIS SUMMARY REPORT ---")
    print(f"[+] Total Critical Events Found: {critical_count}")
    print("=" * 30)

except FileNotFoundError:
    print("[ERROR] The log file was not found.")