#!/usr/bin/env python3
"""
Lists - Storing Multiple Values

WHAT: Lists store multiple items in order
WHERE: Server lists, port numbers, log entries
WHY: DevOps deals with multiple servers, services, configs

REAL-WORLD SCENARIO:
- List of server hostnames
- List of ports to check
- List of backup files
- List of users to create

HOW TO RUN:
    python3 004_lists_basics.py
"""

# Creating a list - use square brackets []
servers = ["web-01", "web-02", "web-03"]
print("Servers:", servers)
print()

# Lists can hold different types
ports = [80, 443, 8080]
print("Ports:", ports)
print()

# Access items by index (position) - starts at 0!
print("First server:", servers[0])   # web-01
print("Second server:", servers[1])  # web-02
print("Third server:", servers[2])   # web-03
print()

# Access from the end - use negative numbers
print("Last server:", servers[-1])    # web-03
print("Second to last:", servers[-2]) # web-02
print()

# How many items in list?
count = len(servers)
print(f"We have {count} servers")
print()

# Add items to list
servers.append("web-04")  # Add to end
print("After adding:", servers)
print()

# Remove items from list
servers.remove("web-02")  # Remove specific item
print("After removing web-02:", servers)
print()

# Check if item exists in list
if "web-01" in servers:
    print("✓ web-01 is in the list")

if "web-99" in servers:
    print("web-99 is in the list")
else:
    print("✗ web-99 is NOT in the list")
print()

# Loop through list (process each item)
print("Processing servers:")
for server in servers:
    print(f"  - Checking {server}")
print()

# Real DevOps example - checking multiple services
services = ["nginx", "mysql", "redis", "docker"]

print("Service Status Check:")
for service in services:
    print(f"  Checking {service}... OK")
print()

# List slicing - get part of a list
environments = ["dev", "test", "staging", "production"]
non_prod = environments[0:3]  # Get items 0, 1, 2 (not 3!)
print("Non-prod environments:", non_prod)
print()

# Sorting lists
unsorted_ports = [8080, 22, 443, 80, 3306]
sorted_ports = sorted(unsorted_ports)
print("Sorted ports:", sorted_ports)
print()

# Combining lists
web_servers = ["web-01", "web-02"]
api_servers = ["api-01", "api-02"]
all_servers = web_servers + api_servers
print("All servers:", all_servers)
print()

# Empty list - useful for collecting results
results = []  # Start empty
results.append("Server 1: OK")
results.append("Server 2: OK")
results.append("Server 3: FAILED")
print("Results:", results)

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Lists are everywhere in DevOps automation!")
print("   Use them for servers, configs, results, etc.")
print("=" * 50)
