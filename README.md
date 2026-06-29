# Cybersecurity Python Toolkit

A collection of practical, hands-on Python scripts developed to explore and apply core cybersecurity concepts. This repository serves as a personal toolkit for security automation, networking, and monitoring.

---

## 🛠️ Included Tools

### 1. File Integrity Monitor (FIM)
A script designed to monitor the integrity of critical system files locally.
* **How it works:** It establishes a baseline by calculating the unique **SHA-256 hash** of a user-specified file. It then runs a continuous loop to check the file every few seconds and triggers real-time alerts if the file is **modified** or **deleted**.
* **File:** `file_monitor.py`

### 2. Network Port Scanner
A lightweight network tool built to identify active services on a target host.
* **How it works:** Utilizing Python's native `socket` library, it attempts to connect to specified ports on a target IP address to determine if they are open or closed.
* **File:** `scanner.py`

### 3. Log Parser & Analyzer
A local log analysis script modeled after core SIEM functions to detect potential threats.
* **How it works:** It opens and reads server log files line by line, filtering for critical keywords like **CRITICAL** or **Failed**. It provides real-time alerts upon discovery and generates an automated summary report counting total security events.
* **File:** `log_parser.py`

---

## 🚀 How to Run

1. Clone this repository or open the project in PyCharm.
2. Ensure you have Python 3 installed.
3. Open your terminal and navigate to the project directory.
4. Run the desired tool:
   ```bash
   # To run the File Integrity Monitor
   python3 file_monitor.py

   # To run the Port Scanner
   python3 scanner.py

   # To run the Log Parser
   python3 log_parser.py