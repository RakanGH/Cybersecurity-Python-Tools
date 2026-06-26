import hashlib
import time


def calculate_file_hash(filepath):
    """Calculates the SHA-256 hash of a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None


# --- Step 2: Get user input for the target file ---
target_file = input("[+] Enter the name of the file to monitor: ").strip()

print(f"[*] Establishing baseline for '{target_file}'...")
baseline_hash = calculate_file_hash(target_file)

if baseline_hash is None:
    print(f"[ERROR] Target file '{target_file}' was not found.")
    print("[*] Please ensure the file exists and restart the script.")
else:
    print(f"[SUCCESS] Baseline established. Current Hash: {baseline_hash}")
    print("[*] Monitoring started... Press Ctrl + C to stop.\n")

    try:
        while True:
            time.sleep(3)
            current_hash = calculate_file_hash(target_file)

            if current_hash is None:
                print(f"[CRITICAL] ALERT: '{target_file}' has been DELETED!")
                break

            elif current_hash != baseline_hash:
                print(f"[WARNING] ALERT: '{target_file}' has been MODIFIED!")
                baseline_hash = current_hash

    except KeyboardInterrupt:
        print("\n[-] Monitoring stopped by user.")