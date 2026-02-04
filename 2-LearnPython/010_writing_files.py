#!/usr/bin/env python3
"""
Writing Files

WHAT: Write data to text files
WHERE: Generate reports, configs, logs
WHY: Save automation results

REAL-WORLD SCENARIO:
- Generate server inventory reports
- Create configuration files
- Write backup manifests
- Save audit results

HOW TO RUN:
    python3 010_writing_files.py
"""

import os
from datetime import datetime

# Method 1: Write to new file (overwrites if exists)
print("Method 1: Writing new file")
output_file = "./report.txt"

with open(output_file, "w") as f:
    f.write("Server Health Report\n")
    f.write("=" * 50 + "\n")
    f.write("Generated: 2026-01-27\n")
    f.write("\n")
    f.write("web-01: HEALTHY\n")
    f.write("web-02: HEALTHY\n")
    f.write("web-03: WARNING\n")

print(f"✓ Created: {output_file}")

# Read back to verify
with open(output_file, "r") as f:
    print(f.read())

print("-" * 50)

# Method 2: Append to existing file (doesn't overwrite)
print("Method 2: Appending to file")

with open(output_file, "a") as f:  # 'a' = append mode
    f.write("\nUpdated: 2026-01-27 14:30\n")
    f.write("api-01: HEALTHY\n")

print("✓ Appended to file")

# Read updated file
with open(output_file, "r") as f:
    print(f.read())

print("-" * 50)

# Real DevOps example 1: Generate inventory CSV
print("Example 1: Generate inventory CSV")

servers = [
    {"name": "web-01", "ip": "10.0.1.10", "status": "running"},
    {"name": "web-02", "ip": "10.0.1.11", "status": "running"},
    {"name": "api-01", "ip": "10.0.2.10", "status": "stopped"}
]

csv_file = "./inventory.csv"
with open(csv_file, "w") as f:
    # Write header
    f.write("Name,IP,Status\n")
    
    # Write data rows
    for server in servers:
        f.write(f"{server['name']},{server['ip']},{server['status']}\n")

print(f"✓ Created CSV: {csv_file}")

# Show content
with open(csv_file, "r") as f:
    print(f.read())

print("-" * 50)

# Real DevOps example 2: Generate configuration file
print("Example 2: Generate config file")

config = {
    "server_name": "web-01",
    "port": 8080,
    "debug": False,
    "max_connections": 1000,
    "timeout": 30
}

config_file = "./app.conf"
with open(config_file, "w") as f:
    f.write("# Application Configuration\n")
    f.write(f"# Generated: {datetime.now()}\n")
    f.write("\n")
    
    for key, value in config.items():
        f.write(f"{key}={value}\n")

print(f"✓ Created config: {config_file}")

# Show content
with open(config_file, "r") as f:
    print(f.read())

print("-" * 50)

# Real DevOps example 3: Write audit log
print("Example 3: Write audit log")

def log_action(action, user, result):
    """Log action to audit file."""
    log_file = "./audit.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {user} - {action} - {result}\n")

# Log some actions
log_action("server_restart", "admin", "SUCCESS")
log_action("backup_create", "backup-user", "SUCCESS")
log_action("config_update", "deployer", "FAILED")

print("✓ Logged actions")

# Show log
log_file = "./audit.log"
with open(log_file, "r") as f:
    print(f.read())

print("-" * 50)

# Real DevOps example 4: Generate HTML report
print("Example 4: Generate HTML report")

html_file = "./report.html"
with open(html_file, "w") as f:
    f.write("<html>\n")
    f.write("<head><title>Server Status</title></head>\n")
    f.write("<body>\n")
    f.write("<h1>Server Status Report</h1>\n")
    f.write("<table border='1'>\n")
    f.write("<tr><th>Server</th><th>Status</th></tr>\n")
    
    for server in servers:
        color = "green" if server["status"] == "running" else "red"
        f.write(f"<tr><td>{server['name']}</td>")
        f.write(f"<td style='color:{color}'>{server['status']}</td></tr>\n")
    
    f.write("</table>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print(f"✓ Created HTML report: {html_file}")
print()

# Write multiple lines at once
print("Example 5: Write multiple lines")

lines = [
    "Server: web-01\n",
    "Status: Running\n",
    "CPU: 45%\n",
    "Memory: 60%\n",
    "Disk: 70%\n"
]

status_file = "./status.txt"
with open(status_file, "w") as f:
    f.writelines(lines)  # Write list of lines

print(f"✓ Created: {status_file}")

# Show content
with open(status_file, "r") as f:
    print(f.read())

# Cleanup
# os.remove(output_file)
# os.remove(csv_file)
# os.remove(config_file)
# os.remove(log_file)
# os.remove(html_file)
# os.remove(status_file)

# DevOps Pro Tip
print("=" * 50)
print("💡 Writing files is essential for automation!")
print("   'w' = write (overwrites)")
print("   'a' = append (adds to end)")
print("   Always use 'with open()' pattern")
print("=" * 50)
