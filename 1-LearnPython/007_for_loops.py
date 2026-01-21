#!/usr/bin/env python3
"""
For Loops - Repeating Actions

WHAT: Repeat code for each item in a list
WHERE: Process multiple servers, files, configs
WHY: Automate repetitive tasks

REAL-WORLD SCENARIO:
- Check status of all servers
- Backup multiple databases
- Process all log files
- Deploy to multiple environments

HOW TO RUN:
    python3 007_for_loops.py
"""

# Basic for loop - iterate over a list
servers = ["web-01", "web-02", "web-03"]

print("Checking servers:")
for server in servers:
    print(f"  Pinging {server}...")

print()

# Loop with numbers - use range()
print("Checking ports:")
for port in range(8080, 8085):  # 8080, 8081, 8082, 8083, 8084
    print(f"  Checking port {port}")

print()

# Loop with index numbers
print("Numbered list:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"  {i}. Server check {i+1}")

print()

# Loop with enumerate - get index AND item
environments = ["dev", "test", "staging", "production"]

print("Deployment order:")
for index, env in enumerate(environments):
    print(f"  Step {index + 1}: Deploy to {env}")

print()

# Real DevOps example 1: Health check
services = ["nginx", "mysql", "redis", "docker"]

print("Service Status:")
for service in services:
    # Simulate checking each service
    status = "running"  # In real script, you'd actually check
    print(f"  ✓ {service}: {status}")

print()

# Real DevOps example 2: Processing multiple servers
servers_info = [
    {"name": "web-01", "ip": "10.0.1.10", "port": 80},
    {"name": "web-02", "ip": "10.0.1.11", "port": 80},
    {"name": "api-01", "ip": "10.0.2.10", "port": 8080}
]

print("Server Configuration:")
for server in servers_info:
    print(f"  {server['name']}: {server['ip']}:{server['port']}")

print()

# Loop with conditions
print("Checking disk usage:")
servers_disk = [
    {"name": "web-01", "disk": 45},
    {"name": "web-02", "disk": 82},
    {"name": "web-03", "disk": 95}
]

for server in servers_disk:
    name = server['name']
    disk = server['disk']
    
    if disk > 90:
        print(f"  🔴 {name}: {disk}% - CRITICAL")
    elif disk > 75:
        print(f"  🟡 {name}: {disk}% - WARNING")
    else:
        print(f"  🟢 {name}: {disk}% - OK")

print()

# Nested loops - loop inside a loop
print("Checking all server ports:")
servers = ["web-01", "web-02"]
ports = [80, 443]

for server in servers:
    print(f"\n{server}:")
    for port in ports:
        print(f"  Checking port {port}... OK")

print()

# Loop through dictionary
server = {
    "hostname": "web-01",
    "ip": "192.168.1.10",
    "port": 8080,
    "status": "running"
}

print("Server details:")
for key, value in server.items():
    print(f"  {key}: {value}")

print()

# Break - stop loop early
print("Finding failed service:")
services_status = ["nginx: OK", "mysql: OK", "redis: FAILED", "docker: OK"]

for service in services_status:
    print(f"  Checking {service}")
    if "FAILED" in service:
        print("  ⚠️  Found failed service! Stopping checks.")
        break  # Exit loop immediately

print()

# Continue - skip to next iteration
print("Processing servers (skip maintenance):")
servers_list = [
    {"name": "web-01", "status": "running"},
    {"name": "web-02", "status": "maintenance"},
    {"name": "web-03", "status": "running"}
]

for server in servers_list:
    if server["status"] == "maintenance":
        print(f"  ⏭️  Skipping {server['name']} (maintenance)")
        continue  # Skip rest of loop, go to next item
    
    print(f"  ✓ Processing {server['name']}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Master for loops - you'll use them constantly!")
print("   Most automation involves processing multiple items")
print("=" * 50)
