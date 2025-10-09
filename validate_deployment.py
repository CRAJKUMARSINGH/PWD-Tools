"""
Validation script for PWD Tools Hub deployment.
This script checks if the environment is properly set up for deployment.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python 3.8+ is installed"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version < (3, 8):
        print("❌ ERROR: Python 3.8 or higher is required")
        return False
    else:
        print("✅ Python version is sufficient")
        return True

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        "app.py",
        "requirements.txt",
        "runtime.txt",
        "config.toml",
        ".streamlit/config.toml",
        "DEPLOYMENT.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ ERROR: Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required files are present")
        return True

def check_required_directories():
    """Check if all required directories exist"""
    required_dirs = [
        "pages",
        "components",
        "utils",
        "static"
    ]
    
    missing_dirs = []
    for directory in required_dirs:
        if not Path(directory).exists():
            missing_dirs.append(directory)
    
    if missing_dirs:
        print(f"❌ ERROR: Missing required directories: {missing_dirs}")
        return False
    else:
        print("✅ All required directories are present")
        return True

def check_dependencies():
    """Check if all required dependencies are installed"""
    with open("requirements.txt", "r") as f:
        required_packages = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]
    
    print(f"Checking {len(required_packages)} required packages...")
    
    missing_packages = []
    for package in required_packages:
        # Handle version specifiers
        package_name = package.split(">")[0].split("<")[0].split("=")[0]
        try:
            __import__(package_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ ERROR: Missing packages: {missing_packages}")
        print("   Run: pip install -r requirements.txt")
        return False
    else:
        print("✅ All required packages are installed")
        return True

def check_streamlit_config():
    """Check Streamlit configuration"""
    config_file = ".streamlit/config.toml"
    if Path(config_file).exists():
        print("✅ Streamlit configuration file exists")
        return True
    else:
        print("❌ ERROR: Streamlit configuration file missing")
        return False

def run_basic_tests():
    """Run basic tests to validate functionality"""
    try:
        # Test importing main modules
        from utils.branding import apply_custom_css
        from components.tool_buttons import create_tool_grid
        print("✅ Core modules can be imported")
        
        # Test if pages directory has content
        pages_dir = Path("pages")
        if pages_dir.exists() and any(pages_dir.iterdir()):
            print("✅ Pages directory has content")
        else:
            print("⚠️  WARNING: Pages directory is empty")
            
        return True
    except Exception as e:
        print(f"❌ ERROR: Failed to import core modules: {e}")
        return False

def main():
    """Main validation function"""
    print("========================================")
    print("PWD Tools Hub Deployment Validation")
    print("========================================")
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_required_files),
        ("Required Directories", check_required_directories),
        ("Dependencies", check_dependencies),
        ("Streamlit Configuration", check_streamlit_config),
        ("Basic Functionality", run_basic_tests)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_function in checks:
        print(f"\n[{check_name}]")
        if check_function():
            passed += 1
        print()
    
    print("========================================")
    print(f"Validation Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("✅ All checks passed! Ready for deployment.")
        return 0
    elif passed >= total * 0.8:
        print("⚠️  Most checks passed. Minor issues detected.")
        return 1
    else:
        print("❌ Critical issues detected. Fix before deployment.")
        return 2

if __name__ == "__main__":
    sys.exit(main())