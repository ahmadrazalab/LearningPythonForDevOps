#!/usr/bin/env python3
"""
Reading Files

WHAT: Read content from text files
WHERE: Parse logs, configs, data files
WHY: Most DevOps data is in files

REAL-WORLD SCENARIO:
- Read log files
- Parse configuration files
- Read server lists
- Process backup manifests

HOW TO RUN:
    python3 009_reading_files.py
"""

import os
import time

# Create a sample file for demonstration
sample_file = "./servers.txt"

# Write sample content
with open(sample_file, "w") as f:
    f.write("web-01\n")
    f.write("web-02\n")
    f.write("web-03\n")
    f.write("api-01\n")
    f.write("api-02\n")

print("Created sample file:", sample_file)
print()

# Method 1: Read entire file at once
print("Method 1: Read entire file")
with open(sample_file, "r") as f:
    content = f.read()
    print(content)

print("-" * 50)

# Method 2: Read line by line (better for large files)
print("Method 2: Read line by line")
with open(sample_file, "r") as f:
    for line in f:
        line = line.strip()  # Remove newline character
        print(f"Server: {line}")
        # time.sleep(1)

print("-" * 50)

# Method 3: Read all lines into a list
print("Method 3: Read into list")
with open(sample_file, "r") as f:
    lines = f.readlines()  # Returns list of lines

print(f"Found {len(lines)} servers:")
for line in lines:
    print(f"  - {line.strip()}")

print("-" * 50)

# Real DevOps example 1: Parse log file
print("Example 1: Parse log file")

# Create sample log file
log_file = "./app.log"
with open(log_file, "w") as f:
    f.write("2026-01-27 10:00:00 INFO Server started\n")
    f.write("2026-01-27 10:01:00 INFO Request received\n")
    f.write("2026-01-27 10:02:00 ERROR Connection timeout\n")
    f.write("2026-01-27 10:03:00 INFO Request completed\n")
    f.write("2026-01-27 10:04:00 ERROR Database unreachable\n")

# Read and find errors
error_count = 0
with open(log_file, "r") as f:
    for line in f:
        if "ERROR" in line:
            print(f"  Found error: {line.strip()}")
            error_count += 1

print(f"Total errors found: {error_count}")
print("-" * 50)

# Real DevOps example 2: Read configuration
print("Example 2: Read configuration")

# Create sample config file
config_file = "./app.conf"
with open(config_file, "w") as f:
    f.write("PORT=8080\n")
    f.write("HOST=0.0.0.0\n")
    f.write("DEBUG=false\n")
    f.write("MAX_CONNECTIONS=100\n")

# Parse config into dictionary
config = {}
with open(config_file, "r") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line:  # Skip empty lines
            key, value = line.split("=")
            config[key] = value

print("Configuration loaded:")
for key, value in config.items():
    print(f"  {key}: {value}")

print("-" * 50)

# Real DevOps example 3: Count statistics
print("Example 3: Count log statistics")

# Create more detailed log
detailed_log = "./detailed.log"
with open(detailed_log, "w") as f:
    f.write("INFO User login successful\n")
    f.write("INFO Database query executed\n")
    f.write("WARNING High memory usage\n")
    f.write("ERROR Connection failed\n")
    f.write("INFO Cache updated\n")
    f.write("ERROR Timeout\n")
    f.write("WARNING Disk space low\n")
    f.write("INFO Backup completed\n")

# Count by level
info_count = 0
warning_count = 0
error_count = 0

with open(detailed_log, "r") as f:
    for line in f:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

print("Log Statistics:")
print(f"  ℹ️  INFO: {info_count}")
print(f"  ⚠️  WARNING: {warning_count}")
print(f"  ❌ ERROR: {error_count}")

print("-" * 50)

# Check if file exists before reading
print("Example 4: Safe file reading")

def read_server_list(filename):
    """Safely read server list file."""
    if not os.path.exists(filename):
        print(f"  ✗ File not found: {filename}")
        return []
    
    servers = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                servers.append(line)
    
    return servers

# Try reading existing file
servers = read_server_list(sample_file)
print(f"Loaded {len(servers)} servers: {servers}")

# Try reading non-existent file
servers = read_server_list("./nonexistent.txt")

# Cleanup
# os.remove(sample_file)
# os.remove(log_file)
# os.remove(config_file)
# os.remove(detailed_log)

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 File operations are core to DevOps!")
print("   Always use 'with open()' - it closes files automatically")
print("   Always check if file exists before reading")
print("=" * 50)
