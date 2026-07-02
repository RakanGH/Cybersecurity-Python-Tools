# Cybersecurity Python Toolkit

A collection of practical, hands-on Python scripts developed to explore and apply core cybersecurity concepts. This repository serves as a personal toolkit for security automation, networking, and monitoring.

---

## 🛠️ Included Tools

### 1. File Integrity Monitor (FIM)
A script designed to monitor the integrity of critical system files locally.
* **File:** `file_monitor.py`

### 2. Network Port Scanner
A lightweight network tool built to identify active services on a target host.
* **File:** `scanner.py`

### 3. Advanced Log Parser & Analyzer
A smart automation script designed to scan server and system logs for potential security threats.
* **Key Features:**
  * **Smart Paths:** Accepts both local file names and full system paths (like `/var/log/auth.log`).
  * **Deep Scan:** Searches for multiple high-risk keywords (`CRITICAL`, `FAILED`, `ERROR`, `WARNING`) regardless of case sensitivity.
  * **Auto-Reporting:** Generates a unique, timestamped text report for every run to preserve history without overwriting previous logs.
* **File:** `log_parser.py`

### 4. SHA-256 Hash Cracker
A dictionary-attack tool built to demonstrate how weak passwords are reconstructed from security hashes.
* **How it works:** It takes a target SHA-256 hash from the user, iterates through a wordlist (`passwords.txt`), converts each plain-text word into a hash, and compares them until a match is found.
* **File:** `hash_cracker.py`

---

## 🚀 How to Run

1. Clone this repository or open the project in PyCharm.
2. Ensure you have Python 3 installed.
3. Open your terminal and navigate to the project directory.
4. Run the desired tool:
   ```bash
   python3 file_monitor.py
   python3 scanner.py
   python3 log_parser.py
   python3 hash_cracker.py