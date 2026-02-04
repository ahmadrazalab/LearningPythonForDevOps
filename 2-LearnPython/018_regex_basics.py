#!/usr/bin/env python3
"""
Regular Expressions (Regex) Basics

WHAT: Pattern matching in text
WHERE: Log parsing, validation, text extraction
WHY: Find patterns in text efficiently

REAL-WORLD SCENARIO:
- Extract IP addresses from logs
- Validate email/phone formats
- Find error patterns in logs
- Extract version numbers
- Parse structured text

HOW TO RUN:
    python3 018_regex_basics.py
"""

import re

# Example 1: Basic pattern matching
print("Example 1: Check if pattern exists")

log_line = "2026-01-27 14:30:00 ERROR Connection timeout"

if re.search("ERROR", log_line):
    print("✓ Found ERROR in log line")

if re.search("SUCCESS", log_line):
    print("Found SUCCESS")
else:
    print("✗ SUCCESS not found")

print()

# Example 2: Extract matches
print("Example 2: Extract matches")

text = "Server IP is 192.168.1.100"
match = re.search(r"\d+\.\d+\.\d+\.\d+", text)  # IP pattern

if match:
    ip = match.group()
    print(f"Found IP address: {ip}")

print()

# Example 3: Find all matches
print("Example 3: Find all matches")

log = "ERROR at line 42, WARNING at line 55, ERROR at line 78"
errors = re.findall("ERROR", log)
print(f"Found {len(errors)} errors")

# Find numbers
numbers = re.findall(r"\d+", log)
print(f"Line numbers: {numbers}")

print()

# Real DevOps example 1: Extract IP addresses
print("Example 4: Extract IP addresses")

log_entries = [
    "Connection from 192.168.1.10",
    "Access denied for 10.0.0.5",
    "Request from 172.16.0.100"
]

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

print("IP addresses found:")
for log in log_entries:
    match = re.search(ip_pattern, log)
    if match:
        print(f"  - {match.group()}")

print()

# Real DevOps example 2: Parse nginx log
print("Example 5: Parse nginx access log")

nginx_log = '192.168.1.10 - - [27/Jan/2026:14:30:00] "GET /api/users HTTP/1.1" 200 1234'

# Extract components
ip = re.search(r"^\d+\.\d+\.\d+\.\d+", nginx_log).group()
date = re.search(r"\[(.*?)\]", nginx_log).group(1)
method = re.search(r'"(\w+)', nginx_log).group(1)
path = re.search(r'"\w+ (\S+)', nginx_log).group(1)
status = re.search(r'" (\d+)', nginx_log).group(1)

print("Parsed log:")
print(f"  IP: {ip}")
print(f"  Date: {date}")
print(f"  Method: {method}")
print(f"  Path: {path}")
print(f"  Status: {status}")

print()

# Real DevOps example 3: Validate formats
print("Example 6: Validate formats")

def validate_email(email):
    """Check if email format is valid."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

emails = [
    "admin@example.com",
    "user.name@company.co.uk",
    "invalid.email",
    "no@domain"
]

print("Email validation:")
for email in emails:
    valid = validate_email(email)
    status = "✓" if valid else "✗"
    print(f"  {status} {email}")

print()

# Real DevOps example 4: Extract version numbers
print("Example 7: Extract version numbers")

outputs = [
    "nginx version: nginx/1.20.1",
    "Python 3.9.7",
    "Docker version 20.10.12, build e91ed57"
]

version_pattern = r"\d+\.\d+\.?\d*"

print("Version numbers:")
for output in outputs:
    match = re.search(version_pattern, output)
    if match:
        print(f"  {match.group()}")

print()

# Real DevOps example 5: Find error patterns
print("Example 8: Find error patterns")

logs = [
    "INFO: Server started successfully",
    "ERROR: Connection refused on port 8080",
    "WARNING: High memory usage detected",
    "ERROR: Database connection timeout",
    "INFO: Request processed in 45ms"
]

error_pattern = r"ERROR: (.+)"

print("Errors found:")
for log in logs:
    match = re.search(error_pattern, log)
    if match:
        error_msg = match.group(1)
        print(f"  - {error_msg}")

print()

# Example 9: Replace patterns
print("Example 9: Replace patterns")

text = "Contact us at old-email@example.com or old-email@test.com"
new_text = re.sub(r"old-email", "new-email", text)
print(f"Original: {text}")
print(f"Updated:  {new_text}")

print()

# Example 10: Split by pattern
print("Example 10: Split by pattern")

data = "web-01,web-02;api-01,api-02"
servers = re.split(r"[,;]", data)  # Split by comma or semicolon

print("Servers:")
for server in servers:
    print(f"  - {server}")

# Common regex patterns
print("\n" + "=" * 50)
print("💡 Common regex patterns:")
print("   \\d = digit (0-9)")
print("   \\w = word character (a-z, A-Z, 0-9, _)")
print("   \\s = whitespace")
print("   . = any character")
print("   * = 0 or more")
print("   + = 1 or more")
print("   ? = 0 or 1")
print("   [abc] = a or b or c")
print("   [0-9] = any digit")
print("   ^ = start of string")
print("   $ = end of string")
print("=" * 50)
