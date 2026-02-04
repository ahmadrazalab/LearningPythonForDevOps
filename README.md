# Python3 for DevOps Engineers - Quick Start Guide

## 🎯 What is Python?

Python is a high-level, interpreted programming language that's become the **de facto standard for DevOps automation**. Unlike compiled languages (Go, Java), Python runs directly without compilation, making it perfect for quick scripts, automation, and infrastructure management.

---

## 📦 Installing Python3

### macOS (your current OS)
```bash
# Check if Python3 is already installed
python3 --version

# Install via Homebrew (recommended)
brew install python3

# Verify installation
which python3
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### Linux (RHEL/CentOS/Amazon Linux)
```bash
sudo yum install python3 python3-pip -y
# OR for newer versions
sudo dnf install python3 python3-pip -y
```

### Verify Installation
```bash
python3 --version    # Should show 3.x.x
pip3 --version       # Should show pip version
```

---

## 🔧 Essential Concepts for DevOps

### 1. **pip - Python Package Manager**

`pip` is like `npm` (Node.js), `apt` (Ubuntu), or `yum` (RHEL) - it installs Python libraries.

```bash
# Install a package
pip3 install requests

# Install multiple packages
pip3 install boto3 pyyaml requests

# Install from requirements file
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Show package details
pip3 show boto3

# Uninstall a package
pip3 uninstall requests

# Upgrade a package
pip3 install --upgrade boto3

# Install specific version
pip3 install boto3==1.26.0
```

### 2. **Virtual Environments (venv) - CRITICAL for Production**

**Why?** Isolate project dependencies, avoid version conflicts, maintain clean systems.

```bash
# Create a virtual environment
python3 -m venv myproject-env

# Activate the environment
source myproject-env/bin/activate    # macOS/Linux
# You'll see (myproject-env) in your prompt

# Now install packages (they go ONLY in this env)
pip install boto3 requests pyyaml

# Deactivate when done
deactivate

# Delete environment (just remove the folder)
rm -rf myproject-env
```

**Real DevOps Use Case:**
```bash
# Project structure
/opt/automation/
  ├── venv/              # Virtual environment
  ├── requirements.txt   # Dependencies
  └── scripts/           # Your Python scripts

# Setup
cd /opt/automation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **requirements.txt - Dependency Management**

Like `package.json` (Node.js) or `Gemfile` (Ruby).

```txt
# requirements.txt
boto3==1.26.137
requests==2.31.0
pyyaml==6.0
kubernetes==26.1.0
python-jenkins==1.8.0
```

```bash
# Generate from current environment
pip freeze > requirements.txt

# Install all dependencies
pip install -r requirements.txt
```

---

## 🚀 Running Python Scripts

### Method 1: Direct Execution
```bash
python3 script.py
```

### Method 2: Make Script Executable (Linux/macOS)
```bash
chmod +x script.py
./script.py
```

Script must start with shebang:
```python
#!/usr/bin/env python3
```

### Method 3: With Arguments
```bash
python3 script.py --env production --region us-east-1
```

---

## 📚 Essential Python Packages for DevOps

### AWS Automation
```bash
pip install boto3           # AWS SDK
pip install awscli          # AWS CLI
```

### Kubernetes
```bash
pip install kubernetes      # K8s Python client
pip install pykubectl       # kubectl wrapper
```

### Configuration & Data
```bash
pip install pyyaml          # YAML parsing
pip install python-dotenv   # .env file support
pip install configparser    # INI file parsing
```

### API & Web
```bash
pip install requests        # HTTP client
pip install urllib3         # HTTP library
pip install fastapi         # API framework
pip install uvicorn         # ASGI server
```

### CI/CD
```bash
pip install python-jenkins  # Jenkins API
pip install python-gitlab   # GitLab API
pip install pygithub        # GitHub API
```

### Monitoring & Logging
```bash
pip install prometheus-client   # Prometheus metrics
pip install elasticsearch       # ELK integration
pip install datadog            # Datadog API
```

### System & Utilities
```bash
pip install paramiko        # SSH client
pip install fabric          # SSH automation
pip install psutil          # System monitoring
pip install python-crontab  # Cron management
```

---

## 🔥 Uvicorn & FastAPI (For Building APIs)

**Use Case:** Build internal APIs, webhooks, health check endpoints.

```bash
# Install
pip install fastapi uvicorn

# Simple API example
# File: api.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

# Run server
uvicorn api:app --host 0.0.0.0 --port 8000 --reload

# Production run
uvicorn api:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 🛠️ Common Python Patterns in DevOps

### 2. Running Shell Commands
```python
import subprocess

result = subprocess.run(
    ['kubectl', 'get', 'pods'],
    capture_output=True,
    text=True
)
print(result.stdout)
```

### 3. Logging (NOT print statements)
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Script started")
logging.error("Something failed")
```

### 4. Exit Codes
```python
import sys

if error_condition:
    logging.error("Critical failure")
    sys.exit(1)  # Non-zero = failure

sys.exit(0)  # Success
```


## Explore More : 
- uvicorn
- uv  (ASGI server).  # npm like tool for python
- gunicorn (WSGI server)
- Django, flask, fastapi
