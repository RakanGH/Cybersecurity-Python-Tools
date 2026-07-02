import os
import datetime

print("=" * 40)
print("     AUTOMATED LOG PARSER TOOL     ")
print("=" * 40)

#  Define current directory at the very top so it's always available
current_directory = os.path.dirname(os.path.abspath(__file__))

# --- Smart Path Input (Local & Absolute) ---
while True:
    user_input = input("[+] Enter the log file name or full path: ").strip()

    # If the user typed a full path (like /var/log/auth.log), use it directly
    if os.path.isabs(user_input):
        log_file = user_input
    else:
        # Otherwise, look for it inside the current project directory
        log_file = os.path.join(current_directory, user_input)

    if os.path.exists(log_file):
        # Extract just the file name for the report title
        file_name = os.path.basename(log_file)
        print(f"[✔] File found! Starting analysis on: {file_name}\n")
        break
    else:
        print(f"[❌] Error: Could not find the file at: {log_file}. Please try again.")

print("-" * 40)

# --- Developed Feature 2: Multiple Keywords & Case Insensitivity ---
KEYWORDS = ["critical", "failed", "error", "invalid", "warning"]
alert_count = 0

# Generate a unique timestamp (e.g., 20260702_153045)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Create a unique report name using just the file name
unique_report_name = f"report_{file_name.split('.')[0]}_{timestamp}.txt"
report_file = os.path.join(current_directory, unique_report_name)

try:
    with open(log_file, "r") as file, open(report_file, "w") as report:

        report.write("=" * 50 + "\n")
        report.write(f"🚨 CYBERSECURITY ALERTS REPORT\n")
        report.write(f"Date of Analysis: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write(f"Analyzed File: {log_file}\n")
        report.write("=" * 50 + "\n\n")

        for line in file:
            line_lower = line.lower()
            match_found = False

            for keyword in KEYWORDS:
                if keyword in line_lower:
                    match_found = True
                    break

            if match_found:
                clean_line = line.strip()
                print(f"[🚨 ALERT] Suspicious event found: {clean_line}")
                report.write(f"[🚨 ALERT] Suspicious event found: {clean_line}\n")
                alert_count += 1

        summary_text = (
                f"\n" + "=" * 40 + "\n"
                                   f"--- ANALYSIS SUMMARY REPORT ---\n"
                                   f"[+] Total Suspicious Events Found: {alert_count}"
                                   f"\n" + "=" * 40 + "\n"
        )

        print(summary_text)
        report.write(summary_text)

    print(f"[✔] Analysis complete. Security report saved to: {unique_report_name}")

except FileNotFoundError:
    print(f"[❌ ERROR] The file '{log_file}' was not found. Please check the path.")
except PermissionError:
    print(
        f"[❌ PERMISSION ERROR] Access denied! You don't have permission to read '{log_file}'.\n[👉 HINT] Try running the script with 'sudo' in your terminal.")
except Exception as e:
    print(f"[❌ UNKNOWN ERROR] An error occurred: {e}")