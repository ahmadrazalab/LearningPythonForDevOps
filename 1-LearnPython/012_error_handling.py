#!/usr/bin/env python3
"""
Error Handling with Try-Except

WHAT: Handle errors gracefully
WHERE: Every production script
WHY: Prevent crashes, handle failures properly

REAL-WORLD SCENARIO:
- File might not exist
- Network connection might fail
- API might return error
- Server might be unreachable

HOW TO RUN:
    python3 012_error_handling.py
"""

# Example 1: Basic try-except
print("Example 1: Handle file not found")

try:
    # Try to read a file that doesn't exist
    with open("/tmp/nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("✗ Error: File not found!")
    print("  Creating default file instead...")

print()

# Example 2: Handle multiple error types
print("Example 2: Multiple error types")

def divide_numbers(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        print(f"  {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("  ✗ Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("  ✗ Error: Invalid input types!")
        return None

divide_numbers(10, 2)   # Works
divide_numbers(10, 0)   # Zero division error
divide_numbers(10, "a") # Type error
print()

# Example 3: Get error message
print("Example 3: Capture error message")

try:
    number = int("not_a_number")
except ValueError as e:
    print(f"✗ Error occurred: {e}")

print()

# Example 4: Finally block (always runs)
print("Example 4: Finally block")

def read_config(filename):
    """Read config file with cleanup."""
    try:
        print(f"  Opening {filename}...")
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"  ✗ File {filename} not found")
        return None
    finally:
        print("  Cleanup completed")  # Always runs

read_config("/tmp/test.txt")
print()

# Real DevOps example 1: Safe API call
print("Example 5: Safe API call")

def check_server(hostname):
    """Check if server is reachable."""
    try:
        # Simulate checking server
        if hostname == "invalid":
            raise ConnectionError("Cannot reach server")
        
        print(f"  ✓ {hostname} is reachable")
        return True
    except ConnectionError as e:
        print(f"  ✗ {hostname}: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Unexpected error: {e}")
        return False

check_server("web-01")
check_server("invalid")
print()

# Real DevOps example 2: Retry with error handling
print("Example 6: Retry logic")

def connect_with_retry(server, max_retries=3):
    """Try to connect with retries."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Attempt {attempt}/{max_retries}...")
            
            # Simulate connection
            if attempt < 3:
                raise ConnectionError("Connection timeout")
            
            print(f"  ✓ Connected to {server}")
            return True
            
        except ConnectionError as e:
            print(f"  ✗ Failed: {e}")
            if attempt == max_retries:
                print(f"  ✗ All {max_retries} attempts failed")
                return False

connect_with_retry("database.local")
print()

# Real DevOps example 3: Safe dictionary access
print("Example 7: Safe dictionary access")

server_info = {
    "hostname": "web-01",
    "ip": "192.168.1.100"
}

# Bad way - might crash
try:
    port = server_info["port"]  # Key doesn't exist!
except KeyError:
    print("✗ Port not found in config")
    port = 8080  # Use default
    print(f"  Using default port: {port}")

# Good way - use .get()
port = server_info.get("port", 8080)
print(f"✓ Port (safe): {port}")
print()

# Raise custom errors
print("Example 8: Custom error")

def validate_port(port):
    """Validate port number."""
    if not isinstance(port, int):
        raise TypeError("Port must be an integer")
    
    if port < 1 or port > 65535:
        raise ValueError(f"Port {port} out of range (1-65535)")
    
    print(f"  ✓ Port {port} is valid")

try:
    validate_port(8080)   # OK
    validate_port(99999)  # Error
except ValueError as e:
    print(f"  ✗ Validation error: {e}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Always handle errors in production scripts!")
print("   Use try-except for risky operations")
print("   Never let scripts crash unexpectedly")
print("   Log errors for debugging")
print("=" * 50)
