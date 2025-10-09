"""
Deployment script for PWD Tools Hub application.
This script handles proper deployment protocols for the Streamlit app.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_python_version():
    """Check if Python 3.8+ is installed"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        return False
    return True

def check_requirements():
    """Check if all required packages are installed"""
    required_packages = [
        "streamlit",
        "pandas", 
        "numpy"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("All required packages are installed")
        return True

def install_requirements():
    """Install required packages from requirements.txt"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def start_development_server():
    """Start the development server"""
    print("Starting PWD Tools Hub development server...")
    print("Application will be available at: http://localhost:8501")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=127.0.0.1"
        ])
    except KeyboardInterrupt:
        print("\nShutting down development server...")
    except Exception as e:
        print(f"Error starting development server: {e}")

def start_production_server():
    """Start the production server"""
    print("Starting PWD Tools Hub production server...")
    print("Application will be available at: http://0.0.0.0:8501")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=0.0.0.0",
            "--server.enableCORS=false",
            "--server.enableXsrfProtection=false"
        ])
    except KeyboardInterrupt:
        print("\nShutting down production server...")
    except Exception as e:
        print(f"Error starting production server: {e}")

def create_deployment_package():
    """Create a deployment package"""
    print("Creating deployment package...")
    
    # Create a deployment directory
    deploy_dir = Path("deployment")
    deploy_dir.mkdir(exist_ok=True)
    
    # Copy necessary files
    files_to_copy = [
        "app.py",
        "requirements.txt",
        "runtime.txt",
        "config.toml"
    ]
    
    dirs_to_copy = [
        "pages",
        "components",
        "utils",
        "static",
        ".streamlit"
    ]
    
    import shutil
    
    for file in files_to_copy:
        if Path(file).exists():
            shutil.copy2(file, deploy_dir)
    
    for directory in dirs_to_copy:
        if Path(directory).exists():
            shutil.copytree(directory, deploy_dir / directory, dirs_exist_ok=True)
    
    print(f"Deployment package created in {deploy_dir}")

def main():
    parser = argparse.ArgumentParser(description="PWD Tools Hub Deployment Script")
    parser.add_argument(
        "--mode",
        choices=["dev", "prod", "package"],
        default="dev",
        help="Deployment mode: dev (development), prod (production), package (create deployment package)"
    )
    parser.add_argument(
        "--install-deps",
        action="store_true",
        help="Install dependencies before starting"
    )
    
    args = parser.parse_args()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies if requested
    if args.install_deps:
        if not install_requirements():
            sys.exit(1)
    
    # Check requirements
    if not check_requirements():
        print("Installing requirements...")
        if not install_requirements():
            sys.exit(1)
    
    # Run based on mode
    if args.mode == "dev":
        start_development_server()
    elif args.mode == "prod":
        start_production_server()
    elif args.mode == "package":
        create_deployment_package()

if __name__ == "__main__":
    main()