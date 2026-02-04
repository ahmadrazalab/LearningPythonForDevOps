#!/usr/bin/env python3
"""
Simple Monitoring Script

WHAT: Combine concepts into a real monitoring script
WHERE: Production monitoring
WHY: Put everything together in a practical example

REAL-WORLD SCENARIO:
Monitor multiple aspects of system health:
- CPU usage
- Memory usage
- Disk space
- Check if services are running
- Generate report

This script combines:
- Functions
- Conditionals
- Loops
- File operations
- Date/time
- Error handling

HOW TO RUN:
    python3 020_simple_monitoring.py
"""

import os
import subprocess
import sys
from datetime import datetime

# ANSI color codes for terminal
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'


def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 60)
    print(f"{BOLD}{title}{RESET}")
    print("=" * 60)


def check_disk_space():
    """Check disk usage."""
    print_header("DISK SPACE CHECK")
    
    try:
        result = subprocess.run(
            ["df", "-h", "/"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            if len(lines) >= 2:
                data_line = lines[1].split()
                usage_percent = int(data_line[4].replace("%", ""))
                
                print(f"Root partition usage: {usage_percent}%")
                
                if usage_percent > 90:
                    print(f"{RED}✗ CRITICAL: Disk usage very high!{RESET}")
                    return False, usage_percent
                elif usage_percent > 75:
                    print(f"{YELLOW}⚠ WARNING: Disk usage high{RESET}")
                    return True, usage_percent
                else:
                    print(f"{GREEN}✓ OK: Disk usage normal{RESET}")
                    return True, usage_percent
    
    except Exception as e:
        print(f"{RED}✗ Error checking disk: {e}{RESET}")
        return False, 0
    
    return False, 0


def check_memory():
    """Check memory usage."""
    print_header("MEMORY CHECK")
    
    try:
        # Try to read /proc/meminfo (Linux)
        if os.path.exists("/proc/meminfo"):
            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()
            
            mem_info = {}
            for line in lines[:3]:  # First 3 lines
                parts = line.split()
                key = parts[0].rstrip(":")
                value = int(parts[1])
                mem_info[key] = value
            
            total = mem_info.get("MemTotal", 0)
            available = mem_info.get("MemAvailable", 0)
            
            if total > 0:
                used_percent = ((total - available) / total) * 100
                print(f"Memory usage: {used_percent:.1f}%")
                
                if used_percent > 90:
                    print(f"{RED}✗ CRITICAL: Memory usage very high!{RESET}")
                    return False
                elif used_percent > 75:
                    print(f"{YELLOW}⚠ WARNING: Memory usage high{RESET}")
                    return True
                else:
                    print(f"{GREEN}✓ OK: Memory usage normal{RESET}")
                    return True
        else:
            print(f"{YELLOW}⚠ Cannot check memory on this system{RESET}")
            return True
    
    except Exception as e:
        print(f"{RED}✗ Error checking memory: {e}{RESET}")
        return False
    
    return True


def check_process(process_name):
    """Check if a process is running."""
    try:
        result = subprocess.run(
            ["pgrep", "-x", process_name],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            pid_count = len(result.stdout.strip().split("\n"))
            print(f"  {GREEN}✓{RESET} {process_name}: running ({pid_count} process{'es' if pid_count > 1 else ''})")
            return True
        else:
            print(f"  {RED}✗{RESET} {process_name}: not running")
            return False
    
    except Exception as e:
        print(f"  {RED}✗{RESET} Error checking {process_name}: {e}")
        return False


def check_services():
    """Check if important services are running."""
    print_header("SERVICE CHECK")
    
    # Common services to check (you can customize)
    services = ["python3"]  # Using python3 as example since it's running this script
    
    all_ok = True
    for service in services:
        if not check_process(service):
            all_ok = False
    
    return all_ok


def generate_report(results):
    """Generate monitoring report file."""
    report_file = "/tmp/system_monitor_report.txt"
    
    try:
        with open(report_file, "w") as f:
            f.write("SYSTEM MONITORING REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            
            f.write("RESULTS:\n")
            f.write(f"  Disk Check: {'PASS' if results['disk'] else 'FAIL'}\n")
            f.write(f"  Memory Check: {'PASS' if results['memory'] else 'FAIL'}\n")
            f.write(f"  Services Check: {'PASS' if results['services'] else 'FAIL'}\n")
            f.write("\n")
            
            f.write("OVERALL STATUS: ")
            if all(results.values()):
                f.write("ALL CHECKS PASSED ✓\n")
            else:
                f.write("SOME CHECKS FAILED ✗\n")
        
        print(f"\n{GREEN}✓{RESET} Report saved to: {report_file}")
        return True
    
    except Exception as e:
        print(f"\n{RED}✗{RESET} Error generating report: {e}")
        return False


def main():
    """Main monitoring function."""
    print(f"\n{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}SYSTEM MONITORING SCRIPT{RESET}")
    print(f"{BOLD}Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"{BOLD}{'=' * 60}{RESET}")
    
    # Run all checks
    results = {}
    
    # Disk check
    disk_ok, disk_usage = check_disk_space()
    results['disk'] = disk_ok
    
    # Memory check
    memory_ok = check_memory()
    results['memory'] = memory_ok
    
    # Services check
    services_ok = check_services()
    results['services'] = services_ok
    
    # Generate report
    print_header("GENERATING REPORT")
    generate_report(results)
    
    # Summary
    print_header("SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"Checks passed: {passed}/{total}")
    
    if all(results.values()):
        print(f"\n{GREEN}{BOLD}✓ ALL CHECKS PASSED{RESET}")
        sys.exit(0)
    else:
        print(f"\n{RED}{BOLD}✗ SOME CHECKS FAILED{RESET}")
        print("\nFailed checks:")
        for check, status in results.items():
            if not status:
                print(f"  {RED}✗{RESET} {check.upper()}")
        sys.exit(1)


if __name__ == "__main__":
    main()
