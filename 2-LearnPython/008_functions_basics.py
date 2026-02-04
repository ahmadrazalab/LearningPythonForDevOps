#!/usr/bin/env python3
"""
Functions - Reusable Code Blocks

WHAT: Package code into reusable chunks
WHERE: Organize automation scripts
WHY: Don't repeat yourself (DRY principle)

REAL-WORLD SCENARIO:
- Check server health (reuse for multiple servers)
- Send notifications (reuse for different events)
- Parse log lines (reuse for many logs)
- Backup database (reuse daily)

HOW TO RUN:
    python3 008_functions_basics.py
"""

# Basic function - no parameters, no return value
def greet():
    """Simple greeting function."""
    print("Hello, DevOps Engineer!")
    print("Ready to automate?")

# Call the function
greet()
print()

# Function with parameters (inputs)
def check_server(server_name):
    """Check a specific server."""
    print(f"Checking {server_name}...")
    print(f"  {server_name} is running")

# Call with different values
check_server("web-01")
check_server("web-02")
check_server("api-01")
print()

# Function with multiple parameters
def deploy_app(app_name, environment, version):
    """Deploy application to environment."""
    print(f"Deploying {app_name} version {version} to {environment}")

deploy_app("my-api", "production", "v1.2.3")
deploy_app("web-app", "staging", "v2.0.0")
print()

# Function with default parameters
def send_alert(message, severity="warning"):
    """Send alert with default severity."""
    print(f"[{severity.upper()}] {message}")

send_alert("Disk usage high")  # Uses default severity
send_alert("Server down", "critical")  # Custom severity
send_alert("Backup completed", "info")
print()

# Function that returns a value
def calculate_usage(used, total):
    """Calculate percentage usage."""
    percentage = (used / total) * 100
    return percentage

# Use the returned value
disk_percent = calculate_usage(80, 100)
print(f"Disk usage: {disk_percent}%")

memory_percent = calculate_usage(12, 16)
print(f"Memory usage: {memory_percent:.1f}%")
print()

# Function returning multiple values
def get_server_info(server_name):
    """Get server information."""
    # In real script, would query actual server
    ip = "192.168.1.100"
    status = "running"
    uptime = "30 days"
    return ip, status, uptime

# Unpack returned values
ip_addr, srv_status, srv_uptime = get_server_info("web-01")
print(f"Server IP: {ip_addr}")
print(f"Status: {srv_status}")
print(f"Uptime: {srv_uptime}")
print()

# Real DevOps example 1: Health check function
def check_health(service_name, cpu, memory, disk):
    """
    Check if service is healthy based on resource usage.
    Returns True if healthy, False if not.
    """
    print(f"Checking {service_name}:")
    print(f"  CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")
    
    # Check thresholds
    if cpu > 90 or memory > 90 or disk > 90:
        print(f"  ✗ {service_name} is UNHEALTHY")
        return False
    else:
        print(f"  ✓ {service_name} is HEALTHY")
        return True

# Use the function
web_healthy = check_health("nginx", 45, 60, 70)
db_healthy = check_health("mysql", 95, 85, 60)
print()

# Real DevOps example 2: Build server URL
def build_url(protocol, hostname, port, path="/"):
    """Build complete URL from parts."""
    url = f"{protocol}://{hostname}:{port}{path}"
    return url

# Build different URLs
web_url = build_url("https", "example.com", 443, "/api/health")
api_url = build_url("http", "api.internal", 8080, "/status")

print("Generated URLs:")
print(f"  Web: {web_url}")
print(f"  API: {api_url}")
print()

# Real DevOps example 3: Validate configuration
def validate_config(config):
    """Validate server configuration dictionary."""
    required_keys = ["hostname", "ip", "port"]
    
    print("Validating configuration...")
    for key in required_keys:
        if key not in config:
            print(f"  ✗ Missing required field: {key}")
            return False
        print(f"  ✓ {key}: {config[key]}")
    
    print("  ✓ Configuration is valid")
    return True

# Test validation
good_config = {
    "hostname": "web-01",
    "ip": "10.0.1.10",
    "port": 80
}

bad_config = {
    "hostname": "web-02"
    # Missing ip and port
}

print("\nConfig 1:")
validate_config(good_config)

print("\nConfig 2:")
validate_config(bad_config)

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Functions make code reusable and organized!")
print("   Write once, use many times")
print("   If you do it twice, make it a function!")
print("=" * 50)
