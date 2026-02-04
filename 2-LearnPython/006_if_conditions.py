#!/usr/bin/env python3
"""
If Statements - Making Decisions

WHAT: Execute code based on conditions
WHERE: Every automation script
WHY: Check status, validate input, handle different scenarios

REAL-WORLD SCENARIO:
- If disk > 90%, send alert
- If service stopped, restart it
- If environment is production, use strict settings
- If error in logs, notify team

HOW TO RUN:
    python3 006_if_conditions.py
"""

# Basic if statement
disk_usage = 85

if disk_usage > 90:
    print("⚠️  CRITICAL: Disk almost full!")

print()

# if-else - handle both cases
service_status = "running"

if service_status == "running":
    print("✓ Service is healthy")
else:
    print("✗ Service is down!")

print()

# if-elif-else - multiple conditions
cpu_usage = 75

if cpu_usage > 90:
    print("🔴 CRITICAL: CPU usage very high")
elif cpu_usage > 70:
    print("🟡 WARNING: CPU usage high")
else:
    print("🟢 OK: CPU usage normal")

print()

# Comparison operators
port = 8080

if port == 8080:
    print("Using port 8080")

if port != 80:
    print("Not using standard HTTP port")

if port > 1024:
    print("Using non-privileged port")

print()

# Multiple conditions - and
environment = "production"
backup_enabled = True

if environment == "production" and backup_enabled:
    print("✓ Production backup is enabled")

# Multiple conditions - or
status = "maintenance"

if status == "stopped" or status == "maintenance":
    print("⚠️  Server is not available")

print()

# Real DevOps example 1: Check server health
memory_usage = 82
disk_usage = 65
cpu_usage = 45

print("Health Check:")
if memory_usage > 90:
    print("  ✗ Memory: CRITICAL")
elif memory_usage > 75:
    print("  ⚠️  Memory: WARNING")
else:
    print("  ✓ Memory: OK")

if disk_usage > 90:
    print("  ✗ Disk: CRITICAL")
elif disk_usage > 75:
    print("  ⚠️  Disk: WARNING")
else:
    print("  ✓ Disk: OK")

if cpu_usage > 90:
    print("  ✗ CPU: CRITICAL")
elif cpu_usage > 75:
    print("  ⚠️  CPU: WARNING")
else:
    print("  ✓ CPU: OK")

print()

# Real DevOps example 2: Environment-specific settings
environment = "production"

if environment == "production":
    debug_mode = False
    log_level = "ERROR"
    max_connections = 1000
    print("Using PRODUCTION settings")
elif environment == "staging":
    debug_mode = True
    log_level = "INFO"
    max_connections = 100
    print("Using STAGING settings")
else:
    debug_mode = True
    log_level = "DEBUG"
    max_connections = 10
    print("Using DEVELOPMENT settings")

print(f"  Debug: {debug_mode}")
print(f"  Log Level: {log_level}")
print(f"  Max Connections: {max_connections}")
print()

# Check if value exists in list
allowed_users = ["admin", "deployer", "monitoring"]
current_user = "admin"

if current_user in allowed_users:
    print(f"✓ Access granted for {current_user}")
else:
    print(f"✗ Access denied for {current_user}")

print()

# Checking for None (nothing/null)
backup_path = None

if backup_path is None:
    print("⚠️  Backup path not configured!")
else:
    print(f"Backup path: {backup_path}")

# Nested if statements
server_type = "web"
has_ssl = True

if server_type == "web":
    print("This is a web server")
    if has_ssl:
        print("  ✓ SSL is enabled")
    else:
        print("  ✗ SSL is NOT enabled - security risk!")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 If statements are the logic of automation!")
print("   Think: 'If this happens, do that'")
print("=" * 50)
