#!/usr/bin/env python3
"""
Running Shell Commands

WHAT: Execute shell commands from Python
WHERE: System administration, automation
WHY: Combine Python logic with shell tools

REAL-WORLD SCENARIO:
- Run 'df -h' to check disk space
- Execute 'systemctl status nginx'
- Run 'aws ec2 describe-instances'
- Execute 'kubectl get pods'

HOW TO RUN:
    python3 015_running_commands.py
"""

import subprocess
import sys

# Example 1: Basic command execution
print("Example 1: Run simple command")

result = subprocess.run(["echo", "Hello from shell!"], capture_output=True, text=True)

print(f"Return code: {result.returncode}")
print(f"Output: {result.stdout}")
print()

# Example 2: Check command success
print("Example 2: Check if command succeeded")

result = subprocess.run(["ls", "/tmp"], capture_output=True, text=True)

if result.returncode == 0:
    print("✓ Command succeeded")
    print("Output:", result.stdout[:100])  # First 100 chars
else:
    print("✗ Command failed")
    print("Error:", result.stderr)

print()

# Example 3: Handle command errors
print("Example 3: Handle errors")

result = subprocess.run(
    ["ls", "/nonexistent"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("✗ Command failed!")
    print(f"Error message: {result.stderr.strip()}")

print()

# Real DevOps example 1: Check disk usage
print("Example 4: Check disk usage")

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    lines = result.stdout.strip().split("\n")
    print("Disk usage for /:")
    print(lines[0])  # Header
    print(lines[1])  # Data
else:
    print("Failed to check disk usage")

print()

# Real DevOps example 2: Get running processes
print("Example 5: Count processes")

result = subprocess.run(
    ["ps", "aux"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    lines = result.stdout.split("\n")
    process_count = len(lines) - 1  # Minus header
    print(f"Running processes: {process_count}")

print()

# Real DevOps example 3: Check service status
print("Example 6: Parse command output")

# Simulate checking a service
result = subprocess.run(
    ["echo", "nginx is running"],
    capture_output=True,
    text=True
)

output = result.stdout.strip()
if "running" in output:
    print("✓ nginx is running")
else:
    print("✗ nginx is not running")

print()

# Example 7: Run shell commands (advanced)
print("Example 7: Run complex shell commands")

# Using shell=True allows shell features like pipes
# But be careful with untrusted input!
result = subprocess.run(
    "echo 'web-01\nweb-02\napi-01' | grep web",
    shell=True,
    capture_output=True,
    text=True
)

print("Web servers:")
print(result.stdout)

# Example 8: Timeout
print("Example 8: Command with timeout")

try:
    result = subprocess.run(
        ["sleep", "2"],
        timeout=1,  # Wait max 1 second
        capture_output=True
    )
except subprocess.TimeoutExpired:
    print("✗ Command timed out!")

print()

# Real DevOps example 4: Safe wrapper function
print("Example 9: Safe command wrapper")

def run_command(command, description=""):
    """
    Safely run a shell command.
    
    Args:
        command: List of command parts
        description: What the command does
    
    Returns:
        Output string if successful, None if failed
    """
    if description:
        print(f"Running: {description}")
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"  ✗ Failed: {result.stderr.strip()}")
            return None
            
    except subprocess.TimeoutExpired:
        print("  ✗ Command timed out")
        return None
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None

# Use the wrapper
output = run_command(["whoami"], "Get current user")
if output:
    print(f"  Current user: {output.strip()}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 subprocess.run() is your friend!")
print("   ✓ capture_output=True to get output")
print("   ✓ text=True for string output")
print("   ✓ Check returncode (0 = success)")
print("   ⚠️  Be careful with shell=True and user input!")
print("=" * 50)
