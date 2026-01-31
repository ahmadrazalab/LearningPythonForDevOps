#!/usr/bin/env python3
"""
File and Directory Operations

WHAT: Work with files and directories
WHERE: File management, cleanup, organization
WHY: Automate file operations

REAL-WORLD SCENARIO:
- Find and delete old log files
- Create backup directories
- Check if config file exists
- List all files in a directory
- Get file size and modification time

HOW TO RUN:
    python3 017_file_operations.py
"""

import os
from datetime import datetime

# Example 1: Check if file/directory exists
print("Example 1: Check existence")

if os.path.exists("/tmp"):
    print("✓ /tmp exists")

if os.path.isfile("/etc/hosts"):
    print("✓ /etc/hosts is a file")

if os.path.isdir("/tmp"):
    print("✓ /tmp is a directory")

print()

# Example 2: Create directories
print("Example 2: Create directories")

test_dir = "/tmp/test_devops"
os.makedirs(test_dir, exist_ok=True)  # exist_ok=True won't error if exists
print(f"✓ Created: {test_dir}")

# Create nested directories
nested_dir = "/tmp/test_devops/logs/2026/01"
os.makedirs(nested_dir, exist_ok=True)
print(f"✓ Created: {nested_dir}")
print()

# Example 3: List directory contents
print("Example 3: List directory contents")

files = os.listdir("/tmp/test_devops")
print(f"Contents of /tmp/test_devops:")
for item in files:
    print(f"  - {item}")

print()

# Example 4: Get file information
print("Example 4: File information")

# Create test file
test_file = "/tmp/test_devops/sample.txt"
with open(test_file, "w") as f:
    f.write("Hello DevOps!")

# Get file size
size = os.path.getsize(test_file)
print(f"File size: {size} bytes")

# Get modification time
mtime = os.path.getmtime(test_file)
mod_time = datetime.fromtimestamp(mtime)
print(f"Modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Get absolute path
abs_path = os.path.abspath(test_file)
print(f"Absolute path: {abs_path}")

print()

# Example 5: Path operations
print("Example 5: Path operations")

path = "/var/log/nginx/access.log"

directory = os.path.dirname(path)
filename = os.path.basename(path)
name, extension = os.path.splitext(filename)

print(f"Full path: {path}")
print(f"Directory: {directory}")
print(f"Filename: {filename}")
print(f"Name: {name}")
print(f"Extension: {extension}")

# Join paths (cross-platform)
backup_path = os.path.join("/backups", "2026", "01", "backup.tar.gz")
print(f"Joined path: {backup_path}")

print()

# Real DevOps example 1: Find files by extension
print("Example 6: Find log files")

def find_files(directory, extension):
    """Find all files with given extension."""
    found_files = []
    
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path) and item.endswith(extension):
            found_files.append(item)
    
    return found_files

# Create some test files
os.makedirs("/tmp/test_devops/logs", exist_ok=True)
for i in range(3):
    with open(f"/tmp/test_devops/logs/app_{i}.log", "w") as f:
        f.write("Log data")

log_files = find_files("/tmp/test_devops/logs", ".log")
print(f"Found {len(log_files)} log files:")
for f in log_files:
    print(f"  - {f}")

print()

# Real DevOps example 2: Get directory size
print("Example 7: Calculate directory size")

def get_directory_size(path):
    """Calculate total size of directory."""
    total_size = 0
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            total_size += get_directory_size(item_path)  # Recursive
    
    return total_size

size = get_directory_size("/tmp/test_devops")
size_kb = size / 1024
print(f"Directory size: {size} bytes ({size_kb:.2f} KB)")

print()

# Real DevOps example 3: Clean old files
print("Example 8: Find old files")

from datetime import timedelta

def find_old_files(directory, days_old):
    """Find files older than N days."""
    old_files = []
    cutoff_time = datetime.now() - timedelta(days=days_old)
    
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            mtime = datetime.fromtimestamp(os.path.getmtime(item_path))
            if mtime < cutoff_time:
                old_files.append((item, mtime))
    
    return old_files

# All our test files are new, so this will show example
old_files = find_old_files("/tmp/test_devops/logs", days_old=30)
print(f"Files older than 30 days: {len(old_files)}")

print()

# Example 9: Rename/move files
print("Example 9: Rename files")

old_name = "/tmp/test_devops/sample.txt"
new_name = "/tmp/test_devops/renamed.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"✓ Renamed: {old_name} → {new_name}")

print()

# Example 10: Delete files and directories
print("Example 10: Delete files")

# Delete a file
if os.path.exists(new_name):
    os.remove(new_name)
    print(f"✓ Deleted file: {new_name}")

# Delete empty directory
empty_dir = "/tmp/test_devops/empty"
os.makedirs(empty_dir, exist_ok=True)
os.rmdir(empty_dir)
print(f"✓ Deleted empty directory: {empty_dir}")

# Delete directory with contents
import shutil
if os.path.exists("/tmp/test_devops"):
    shutil.rmtree("/tmp/test_devops")
    print(f"✓ Deleted directory tree: /tmp/test_devops")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 File operations are fundamental to DevOps!")
print("   os.path.exists() - check if exists")
print("   os.makedirs() - create directories")
print("   os.listdir() - list contents")
print("   os.path.join() - join paths safely")
print("   os.remove() - delete file")
print("   shutil.rmtree() - delete directory")
print("=" * 50)
