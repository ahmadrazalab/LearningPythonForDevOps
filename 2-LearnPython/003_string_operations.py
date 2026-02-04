#!/usr/bin/env python3
"""
String Operations for DevOps

WHAT: Learn to manipulate strings (text)
WHERE: Log parsing, server names, building commands
WHY: 90% of DevOps automation involves processing text

REAL-WORLD SCENARIO:
- Parse log lines
- Build server hostnames
- Format output messages
- Extract information from text

HOW TO RUN:
    python3 003_string_operations.py
"""

# String concatenation - joining strings together
first_name = "nginx"
last_name = "server"
full_name = first_name + "-" + last_name
print("Full name:", full_name)  # nginx-server
print()

# String formatting - modern way (f-strings)
environment = "production"
region = "us-east-1"
server_id = 42

# f-string - put f before the quote, use {variable} inside
message = f"Server {server_id} in {environment} ({region})"
print(message)
print()

# Real DevOps examples
hostname = "web-server"
number = 5
full_hostname = f"{hostname}-{number:02d}"  # 02d = 2-digit number with leading zero
print("Hostname:", full_hostname)  # web-server-05
print()

# String methods (functions that work on strings)
log_line = "  ERROR: Connection timeout  "

# Remove extra spaces
cleaned = log_line.strip()
print("Cleaned:", cleaned)

# Convert to lowercase
lower = log_line.lower()
print("Lowercase:", lower)

# Convert to uppercase
upper = log_line.upper()
print("Uppercase:", upper)

# Check if string contains text
if "ERROR" in log_line:
    print("Found an error in the log!")

if "SUCCESS" in log_line:
    print("Found success")
else:
    print("No success found")
print()

# Split string into parts
servers = "web-01,web-02,web-03"
server_list = servers.split(",")  # Split by comma
print("Server list:", server_list)
print()

# Replace text
old_url = "http://old-server.com/api"
new_url = old_url.replace("old-server", "new-server")
print("Old URL:", old_url)
print("New URL:", new_url)
print()

# Check if string starts or ends with something
filename = "backup-2026-01-27.tar.gz"

if filename.startswith("backup"):
    print("This is a backup file")

if filename.endswith(".tar.gz"):
    print("This is a compressed archive")
print()

# Multi-line strings (useful for configs)
config = """
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
}
"""
print("Nginx config:")
print(config)

# DevOps Pro Tip
print("=" * 50)
print("💡 Master string operations - you'll use them daily!")
print("=" * 50)
