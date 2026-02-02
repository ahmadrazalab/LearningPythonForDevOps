#!/usr/bin/env python3
"""
HTTP Requests Basics

WHAT: Make HTTP requests to APIs
WHERE: API calls, health checks, webhooks
WHY: Interact with web services and APIs

REAL-WORLD SCENARIO:
- Check if service is up (health check)
- Call REST APIs
- Send webhook notifications
- Download files
- Query external services

NOTE: Requires 'requests' library
Install: pip3 install requests

HOW TO RUN:
    python3 019_http_requests.py
"""

# Try to import requests
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("⚠️  'requests' library not installed")
    print("Install it with: pip3 install requests")
    print()
    print("This script will show examples without actually running them.")
    print()

# Example 1: Basic GET request
print("Example 1: Basic GET request")
print("Code:")
print("  response = requests.get('https://api.github.com')")
print("  print(response.status_code)  # 200 = success")
print("  print(response.text)         # Response body")

if HAS_REQUESTS:
    try:
        response = requests.get("https://api.github.com")
        print(f"\n✓ Status: {response.status_code}")
        print(f"  Response size: {len(response.text)} bytes")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "-" * 50 + "\n")

# Example 2: Check status code
print("Example 2: Check if request succeeded")
print("Code:")
print("  response = requests.get('https://example.com')")
print("  if response.status_code == 200:")
print("      print('Success!')")
print("  else:")
print("      print('Failed')")

if HAS_REQUESTS:
    try:
        response = requests.get("https://httpbin.org/status/200")
        if response.status_code == 200:
            print("\n✓ Request succeeded")
        else:
            print(f"\n✗ Request failed: {response.status_code}")
    except Exception as e:
        print(f"\n✗ Error: {e}")

print("\n" + "-" * 50 + "\n")

# Example 3: Parse JSON response
print("Example 3: Parse JSON response")
print("Code:")
print("  response = requests.get('https://api.github.com/users/github')")
print("  data = response.json()")
print("  print(data['name'])")

if HAS_REQUESTS:
    try:
        response = requests.get("https://api.github.com/users/github")
        data = response.json()
        print(f"\n✓ Got JSON data")
        print(f"  Name: {data.get('name', 'N/A')}")
        print(f"  Public repos: {data.get('public_repos', 'N/A')}")
    except Exception as e:
        print(f"\n✗ Error: {e}")

print("\n" + "-" * 50 + "\n")

# Real DevOps example 1: Health check
print("Example 4: Service health check")
print('''Code:
  def check_health(url):
      """Check if service is healthy."""
      try:
          response = requests.get(url, timeout=5)
          if response.status_code == 200:
              return True, "Healthy"
          else:
              return False, f"Status {response.status_code}"
      except Exception as e:
          return False, str(e)
  
  healthy, message = check_health("https://example.com")
  print(f"Status: {message}")
''')

if HAS_REQUESTS:
    def check_health(url):
        """Check if service is healthy."""
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True, "Healthy"
            else:
                return False, f"Status {response.status_code}"
        except Exception as e:
            return False, str(e)
    
    print("Testing health checks:")
    services = [
        ("GitHub", "https://api.github.com"),
        ("HTTPBin", "https://httpbin.org/status/200")
    ]
    
    for name, url in services:
        healthy, message = check_health(url)
        status = "✓" if healthy else "✗"
        print(f"  {status} {name}: {message}")

print("\n" + "-" * 50 + "\n")

# Example 5: POST request
print("Example 5: POST request")
print('''Code:
  # Send data to API
  data = {"name": "web-01", "status": "running"}
  response = requests.post(
      "https://api.example.com/servers",
      json=data,
      headers={"Content-Type": "application/json"}
  )
  print(response.status_code)
''')

if HAS_REQUESTS:
    try:
        # httpbin.org echoes back what you send
        data = {"server": "web-01", "status": "running"}
        response = requests.post("https://httpbin.org/post", json=data)
        print(f"\n✓ POST request sent")
        print(f"  Status: {response.status_code}")
    except Exception as e:
        print(f"\n✗ Error: {e}")

print("\n" + "-" * 50 + "\n")

# Example 6: Request with headers
print("Example 6: Request with custom headers")
print('''Code:
  headers = {
      "Authorization": "Bearer YOUR_TOKEN",
      "User-Agent": "MyDevOpsScript/1.0"
  }
  response = requests.get("https://api.example.com", headers=headers)
''')

print("\n" + "-" * 50 + "\n")

# Example 7: Request with timeout
print("Example 7: Request with timeout")
print('''Code:
  try:
      response = requests.get("https://example.com", timeout=5)
  except requests.Timeout:
      print("Request timed out!")
''')

print("\n" + "-" * 50 + "\n")

# Real DevOps example 2: Send Slack notification
print("Example 8: Send Slack webhook (example)")
print('''Code:
  def send_slack_alert(webhook_url, message):
      """Send alert to Slack."""
      payload = {
          "text": message
      }
      response = requests.post(webhook_url, json=payload)
      return response.status_code == 200
  
  webhook = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
  send_slack_alert(webhook, "Server web-01 is down!")
''')

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 HTTP requests are essential for DevOps!")
print("   requests.get() - GET request")
print("   requests.post() - POST request")
print("   response.status_code - HTTP status (200, 404, etc)")
print("   response.json() - Parse JSON response")
print("   timeout= - Always set timeouts!")
print("\n   Install: pip3 install requests")
print("=" * 50)
