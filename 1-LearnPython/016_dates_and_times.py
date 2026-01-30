#!/usr/bin/env python3
"""
Working with Dates and Times

WHAT: Handle dates, times, and timestamps
WHERE: Logs, backups, scheduling, monitoring
WHY: Track when things happen

REAL-WORLD SCENARIO:
- Timestamp log entries
- Check if backup is old
- Calculate uptime
- Schedule maintenance windows
- Parse log timestamps

HOW TO RUN:
    python3 016_dates_and_times.py
"""

from datetime import datetime, timedelta
import time

# Example 1: Current date and time
print("Example 1: Current date/time")

now = datetime.now()
print(f"Current datetime: {now}")
print(f"Date: {now.date()}")
print(f"Time: {now.time()}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print()

# Example 2: Format dates
print("Example 2: Format dates")

timestamp = datetime.now()

# Common formats
print(f"ISO format: {timestamp.isoformat()}")
print(f"Date only: {timestamp.strftime('%Y-%m-%d')}")
print(f"Time only: {timestamp.strftime('%H:%M:%S')}")
print(f"Full: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Readable: {timestamp.strftime('%B %d, %Y at %I:%M %p')}")
print()

# Example 3: Parse date strings
print("Example 3: Parse date strings")

date_string = "2026-01-27 14:30:00"
parsed = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed}")
print()

# Example 4: Date arithmetic
print("Example 4: Date calculations")

now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
three_hours_ago = now - timedelta(hours=3)

print(f"Now: {now.strftime('%Y-%m-%d %H:%M')}")
print(f"Yesterday: {yesterday.strftime('%Y-%m-%d %H:%M')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d %H:%M')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d %H:%M')}")
print(f"3 hours ago: {three_hours_ago.strftime('%Y-%m-%d %H:%M')}")
print()

# Real DevOps example 1: Check backup age
print("Example 5: Check backup age")

backup_time = datetime.now() - timedelta(hours=26)
age_hours = (datetime.now() - backup_time).total_seconds() / 3600

print(f"Last backup: {backup_time.strftime('%Y-%m-%d %H:%M')}")
print(f"Age: {age_hours:.1f} hours")

if age_hours > 24:
    print("⚠️  Backup is more than 24 hours old!")
else:
    print("✓ Backup is recent")

print()

# Real DevOps example 2: Log timestamp
print("Example 6: Generate log entries")

def log(level, message):
    """Log message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

log("INFO", "Server started")
time.sleep(1)
log("INFO", "Processing request")
time.sleep(1)
log("ERROR", "Connection timeout")
print()

# Real DevOps example 3: Calculate uptime
print("Example 7: Calculate uptime")

start_time = datetime.now() - timedelta(days=30, hours=5, minutes=23)
uptime = datetime.now() - start_time

days = uptime.days
hours = uptime.seconds // 3600
minutes = (uptime.seconds % 3600) // 60

print(f"Server started: {start_time.strftime('%Y-%m-%d %H:%M')}")
print(f"Uptime: {days} days, {hours} hours, {minutes} minutes")
print()

# Example 8: Unix timestamp
print("Example 8: Unix timestamps")

# Current timestamp
unix_timestamp = time.time()
print(f"Unix timestamp: {unix_timestamp}")

# Convert to datetime
dt = datetime.fromtimestamp(unix_timestamp)
print(f"Datetime: {dt}")

# Convert datetime to timestamp
timestamp = dt.timestamp()
print(f"Back to timestamp: {timestamp}")
print()

# Real DevOps example 4: Check maintenance window
print("Example 9: Check maintenance window")

now = datetime.now()
maintenance_start = now.replace(hour=2, minute=0, second=0)
maintenance_end = now.replace(hour=4, minute=0, second=0)

print(f"Current time: {now.strftime('%H:%M')}")
print(f"Maintenance window: {maintenance_start.strftime('%H:%M')} - {maintenance_end.strftime('%H:%M')}")

if maintenance_start <= now <= maintenance_end:
    print("⚠️  Currently in maintenance window")
else:
    print("✓ Outside maintenance window")

print()

# Real DevOps example 5: Generate backup filename
print("Example 10: Generate timestamped filename")

def generate_backup_name(service):
    """Generate backup filename with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{service}_{timestamp}.tar.gz"

backup_file = generate_backup_name("database")
print(f"Backup filename: {backup_file}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Dates and times are crucial in DevOps!")
print("   Common formats:")
print("   %Y = 4-digit year (2026)")
print("   %m = month (01-12)")
print("   %d = day (01-31)")
print("   %H = hour (00-23)")
print("   %M = minute (00-59)")
print("   %S = second (00-59)")
print("=" * 50)
