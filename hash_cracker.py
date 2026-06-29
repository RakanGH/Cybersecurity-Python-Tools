import hashlib
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
wordlist_path = os.path.join(current_directory, "passwords.txt")

# 1. Ask the user to input the target SHA-256 hash to crack
target_hash = input("[+] Enter the SHA-256 hash to crack: ").strip()

print("[*] Starting brute-force/dictionary attack...\n")

# A variable to keep track if we found the password or not
password_found = False

try:
    with open(wordlist_path, "r") as file:
        for line in file:
            password = line.strip()

            # Convert password to SHA-256 hash
            password_bytes = password.encode("utf-8")
            current_hash = hashlib.sha256(password_bytes).hexdigest()

            # 2. Compare the current hash with the target hash
            if current_hash == target_hash:
                print(f"[ SUCCESS] Password found: {password}")
                password_found = True
                break  # Stop the loop immediately since we found it

    # 3. If we checked all words and found nothing
    if not password_found:
        print("[-] Password not found in the wordlist.")

except FileNotFoundError:
    print("[ERROR] The file 'passwords.txt' was not found.")