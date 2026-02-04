#!/usr/bin/env python3
"""
Variables and Data Types

WHAT: Learn how to store data in variables
WHERE: Foundation for all DevOps scripts
WHY: You need to store server names, ports, IPs, etc.

REAL-WORLD SCENARIO:
Every automation script uses variables to store:
- Server hostnames
- Port numbers
- Configuration values
- Status information

HOW TO RUN:
    python3 002_variables_and_types.py
"""

# STRINGS - Text data (server names, IPs, etc.)
# Use quotes (single or double)
server_name = "web-server-01"
environment = 'production'
ip_address = "192.168.1.100"

print("Server Name:", server_name)
print("Environment:", environment)
print("IP Address:", ip_address)
print()

# INTEGERS - Whole numbers (ports, counts, etc.)
port = 8080
server_count = 5
retry_attempts = 3

print("Port:", port)
print("Server Count:", server_count)
print("Retry Attempts:", retry_attempts)
print()

# FLOATS - Decimal numbers (percentages, measurements)
cpu_usage = 75.5
memory_gb = 16.0
disk_usage_percent = 82.3

print("CPU Usage:", cpu_usage, "%")
print("Memory:", memory_gb, "GB")
print("Disk Usage:", disk_usage_percent, "%")
print()

# BOOLEANS - True/False values (status checks)
is_running = True
is_healthy = True
maintenance_mode = False

print("Server Running?", is_running)
print("Server Healthy?", is_healthy)
print("Maintenance Mode?", maintenance_mode)
print()

# You can change variable values
status = "starting"
print("Status:", status)

status = "running"  # Changed value
print("Status:", status)

status = "stopped"  # Changed again
print("Status:", status)
print()

# Variable naming rules for DevOps
# ✓ Good names (clear and descriptive)
max_connections = 100
database_host = "db.example.com"
backup_enabled = True

# ✗ Bad names (unclear)
# x = 100
# h = "db.example.com"
# flag = True

# DevOps tip: Use descriptive variable names
# Someone else (or future you) will read this code!
print("=" * 50)
print("✓ Always use clear, descriptive variable names!")
print("=" * 50)
