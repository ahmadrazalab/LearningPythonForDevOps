#!/usr/bin/env python3
"""
Command Line Arguments

WHAT: Accept input from command line
WHERE: Make scripts flexible and reusable
WHY: Same script, different inputs

REAL-WORLD SCENARIO:
- ./backup.py --database mydb --output /backups
- ./deploy.py --env production --version v1.2.3
- ./check-health.py --server web-01 --port 8080

HOW TO RUN:
    python3 013_cli_arguments.py
    python3 013_cli_arguments.py web-01
    python3 013_cli_arguments.py web-01 production
"""

import sys

# Example 1: Basic arguments
print("Example 1: Basic arguments")
print(f"Script name: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv)}")
print(f"All arguments: {sys.argv}")
print()

# Example 2: Using arguments
if len(sys.argv) > 1:
    server_name = sys.argv[1]
    print(f"Checking server: {server_name}")
else:
    print("No server specified")
    print("Usage: python3 013_cli_arguments.py <server-name>")

print()

# Example 3: Multiple arguments
print("Example 2: Multiple arguments")
if len(sys.argv) >= 3:
    server = sys.argv[1]
    environment = sys.argv[2]
    print(f"Deploying to {server} in {environment}")
else:
    print("Usage: python3 013_cli_arguments.py <server> <environment>")

print()

# Real DevOps example: Simple deployment script
print("Example 3: Simple deployment script")

def deploy(server, env="dev", version="latest"):
    """Deploy application."""
    print(f"Deploying to {server}")
    print(f"  Environment: {env}")
    print(f"  Version: {version}")

# Parse arguments
if len(sys.argv) >= 2:
    srv = sys.argv[1]
    env = sys.argv[2] if len(sys.argv) >= 3 else "dev"
    ver = sys.argv[3] if len(sys.argv) >= 4 else "latest"
    deploy(srv, env, ver)
else:
    print("Usage: python3 013_cli_arguments.py <server> [environment] [version]")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Command line arguments make scripts reusable!")
print("   sys.argv[0] = script name")
print("   sys.argv[1] = first argument")
print("   sys.argv[2] = second argument")
print("   For advanced CLI, use 'argparse' module")
print("=" * 50)
