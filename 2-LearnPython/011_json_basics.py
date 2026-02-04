#!/usr/bin/env python3
"""
Working with JSON

WHAT: Parse and create JSON data
WHERE: API responses, config files, data exchange
WHY: JSON is the standard format for APIs and configs

REAL-WORLD SCENARIO:
- Parse AWS CLI output (JSON)
- Read/write configuration files
- Process API responses
- Store structured data

HOW TO RUN:
    python3 011_json_basics.py
"""

# | Function       | What it does                                |
# | -------------- | ------------------------------------------- |
# | `json.dumps()` | Python object → **JSON string (in memory)** |
# | `json.dump()`  | Python object → **JSON file (on disk)**     |
# | `json.loads()` | JSON string → **Python object (in memory)** |
# | `json.load()`  | JSON file → **Python object (on disk)**     |



import json

# Convert Python dictionary to JSON string
print("Example 1: Python to JSON")
server = {
    "hostname": "web-01",
    "ip": "192.168.1.100",
    "port": 8080,
    "services": ["nginx", "docker"],
    "active": True
}

json_string = json.dumps(server)
print("JSON string:", json_string)
print()

# Pretty print JSON (with indentation)
json_pretty = json.dumps(server, indent=2)
print("Pretty JSON:")
print(json_pretty)
print()

# Convert JSON string to Python dictionary
print("Example 2: JSON to Python")
json_data = '{"name": "api-01", "status": "running", "port": 3000}'
python_dict = json.loads(json_data)

print("Python dict:", python_dict)
print("Name:", python_dict["name"])
print("Status:", python_dict["status"])
print()

# Write JSON to file
print("Example 3: Write JSON file")
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "cache": {
        "host": "redis.local",
        "port": 6379
    }
}

with open("./config.json", "w") as f:
    json.dump(config, f, indent=2)

print("✓ Wrote config.json")
print()

# Read JSON from file
print("Example 4: Read JSON file")
with open("./config.json", "r") as f:
    loaded_config = json.load(f)

print("Loaded config:")
print(f"  Database: {loaded_config['database']['host']}:{loaded_config['database']['port']}")
print(f"  Cache: {loaded_config['cache']['host']}:{loaded_config['cache']['port']}")
print()

# Real DevOps example: Parse API response
print("Example 5: Parse API response")
api_response = '''
{
  "instances": [
    {"id": "i-123", "type": "t3.medium", "state": "running"},
    {"id": "i-456", "type": "t3.large", "state": "stopped"},
    {"id": "i-789", "type": "t3.small", "state": "running"}
  ]
}
'''

data = json.loads(api_response)
print(f"Found {len(data['instances'])} instances:")
for instance in data['instances']:
    status_icon = "✓" if instance["state"] == "running" else "✗"
    print(f"  {status_icon} {instance['id']}: {instance['type']} - {instance['state']}")

import os
# os.remove("/tmp/config.json")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 JSON is everywhere in DevOps!")
print("   json.dumps() = Python → JSON string")
print("   json.loads() = JSON string → Python")
print("   json.dump() = Python → JSON file")
print("   json.load() = JSON file → Python")
print("=" * 50)
