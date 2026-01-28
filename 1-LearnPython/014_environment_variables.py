#!/usr/bin/env python3
"""
Environment Variables

WHAT: Read system environment variables
WHERE: Configuration, secrets, API keys
WHY: Don't hardcode sensitive data

REAL-WORLD SCENARIO:
- API keys (AWS_ACCESS_KEY_ID)
- Database passwords
- Environment names (ENVIRONMENT=production)
- Feature flags

HOW TO RUN:
    python3 014_environment_variables.py
    ENVIRONMENT=production python3 014_environment_variables.py
    export API_KEY=secret123 && python3 014_environment_variables.py
"""

import os

# Example 1: Read environment variable
print("Example 1: Read environment variable")

environment = os.getenv("ENVIRONMENT")
if environment:
    print(f"Environment: {environment}")
else:
    print("Environment: Not set (defaulting to 'dev')")

print()

# Example 2: Read with default value
print("Example 2: Default values")

env = os.getenv("ENVIRONMENT", "development")
region = os.getenv("AWS_REGION", "us-east-1")
debug = os.getenv("DEBUG", "false")

print(f"Environment: {env}")
print(f"Region: {region}")
print(f"Debug: {debug}")
print()

# Example 3: Check if variable exists
print("Example 3: Check existence")

if "DATABASE_URL" in os.environ:
    db_url = os.environ["DATABASE_URL"]
    print(f"Database URL: {db_url}")
else:
    print("✗ DATABASE_URL not set")

print()

# Example 4: Get all environment variables
print("Example 4: List environment variables")
print("Common environment variables:")
for key in ["HOME", "USER", "PATH", "SHELL"]:
    value = os.getenv(key, "Not set")
    if key == "PATH":
        value = value[:50] + "..." if len(value) > 50 else value
    print(f"  {key}: {value}")

print()

# Real DevOps example 1: Configuration from env
print("Example 5: Load configuration")

class Config:
    """Application configuration from environment."""
    
    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "dev")
        self.port = int(os.getenv("PORT", "8080"))
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
        self.database_host = os.getenv("DB_HOST", "localhost")
        self.database_port = int(os.getenv("DB_PORT", "5432"))
    
    def show(self):
        print("Configuration:")
        print(f"  Environment: {self.environment}")
        print(f"  Port: {self.port}")
        print(f"  Debug: {self.debug}")
        print(f"  Database: {self.database_host}:{self.database_port}")

config = Config()
config.show()
print()

# Real DevOps example 2: Environment-specific settings
print("Example 6: Environment-specific behavior")

env = os.getenv("ENVIRONMENT", "dev")

if env == "production":
    print("🔴 PRODUCTION MODE")
    print("  - Debug: Disabled")
    print("  - Logging: ERROR level")
    print("  - Backups: Enabled")
elif env == "staging":
    print("🟡 STAGING MODE")
    print("  - Debug: Enabled")
    print("  - Logging: INFO level")
    print("  - Backups: Disabled")
else:
    print("🟢 DEVELOPMENT MODE")
    print("  - Debug: Enabled")
    print("  - Logging: DEBUG level")
    print("  - Backups: Disabled")

print()

# Set environment variable (for current process only)
print("Example 7: Set environment variable")
os.environ["MY_VAR"] = "test_value"
print(f"MY_VAR: {os.getenv('MY_VAR')}")

# DevOps Pro Tip
print("\n" + "=" * 50)
print("💡 Use environment variables for configuration!")
print("   ✓ API keys and secrets")
print("   ✓ Environment names (dev/prod)")
print("   ✓ Database URLs")
print("   ✓ Feature flags")
print("   ✗ Don't hardcode secrets in code!")
print("=" * 50)
