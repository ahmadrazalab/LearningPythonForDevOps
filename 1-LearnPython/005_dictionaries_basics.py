#!/usr/bin/env python3
"""
Dictionaries - Key-Value Pairs

WHAT: Store data as key-value pairs (like JSON)
WHERE: Configuration, server info, API responses
WHY: Perfect for structured data

REAL-WORLD SCENARIO:
- Server configurations (hostname, IP, port)
- AWS instance details
- API responses
- Environment variables

HOW TO RUN:
    python3 005_dictionaries_basics.py
"""

# Creating a dictionary - use curly braces {}
# Format: {key: value, key: value}
server = {
    "hostname": "web-server-01",
    "ip": "192.168.1.100",
    "port": 8080,
    "status": "running"
}

print("Server info:", server)
print()

# Access values by key
print("Hostname:", server["hostname"])
print("IP Address:", server["ip"])
print("Port:", server["port"])
print("Status:", server["status"])
print()

# Change values
server["status"] = "stopped"
print("New status:", server["status"])
print()

# Add new key-value pairs
server["environment"] = "production"
server["region"] = "us-east-1"
print("Updated server:", server)
print()

# Check if key exists
if "hostname" in server:
    print("✓ Hostname is defined")

if "database" in server:
    print("Database is defined")
else:
    print("✗ Database is NOT defined")
print()

# Get value safely (won't crash if key missing)
cpu_usage = server.get("cpu", "N/A")  # Returns "N/A" if not found
print("CPU Usage:", cpu_usage)
print()

# Real DevOps example - multiple servers
web_01 = {
    "name": "web-01",
    "type": "nginx",
    "memory_gb": 8,
    "cpu_cores": 4
}

web_02 = {
    "name": "web-02",
    "type": "nginx",
    "memory_gb": 16,
    "cpu_cores": 8
}

print(f"{web_01['name']}: {web_01['cpu_cores']} cores, {web_01['memory_gb']}GB RAM")
print(f"{web_02['name']}: {web_02['cpu_cores']} cores, {web_02['memory_gb']}GB RAM")
print()

# Loop through dictionary keys
print("Server properties:")
for key in server:
    print(f"  {key}: {server[key]}")
print()

# Loop through keys and values together
print("Server details:")
for key, value in server.items():
    print(f"  {key} = {value}")
print()

# Nested dictionaries (dictionary inside dictionary)
infrastructure = {
    "web_servers": {
        "count": 3,
        "type": "t3.medium"
    },
    "databases": {
        "count": 2,
        "type": "db.t3.large"
    }
}

print("Web servers:", infrastructure["web_servers"])
print("Web server type:", infrastructure["web_servers"]["type"])
print()

# List of dictionaries - very common in DevOps!
servers = [
    {"name": "web-01", "status": "running"},
    {"name": "web-02", "status": "running"},
    {"name": "web-03", "status": "stopped"}
]

print("Server Status Report:")
for server in servers:
    status_icon = "✓" if server["status"] == "running" else "✗"
    print(f"  {status_icon} {server['name']}: {server['status']}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Dictionaries are like JSON - perfect for configs!")
print("   Most APIs return data as dictionaries")
print("=" * 50)



