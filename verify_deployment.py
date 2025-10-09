"""
Verification script to ensure all deployment requirements are met.
"""

import os
import sys

def check_required_files():
    """Check that all required files for deployment exist"""
    required_files = [
        "app.py",
        "streamlit_app.py",
        "requirements.txt",
        "runtime.txt",
        "README.md",
        "DEPLOYMENT.md",
        "config.toml"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True

def check_streamlit_config():
    """Check that Streamlit configuration directory exists"""
    config_dir = ".streamlit"
    config_file = os.path.join(config_dir, "config.toml")
    
    if os.path.exists(config_dir) and os.path.exists(config_file):
        print("✅ Streamlit configuration present")
        return True
    else:
        print("❌ Streamlit configuration missing")
        return False

def check_entry_points():
    """Check that entry points are properly configured"""
    # Check app.py
    try:
        with open("app.py", "r") as f:
            app_content = f.read()
        if "def main():" in app_content and "if __name__ == \"__main__\"" in app_content:
            print("✅ app.py entry point properly configured")
        else:
            print("❌ app.py entry point issues")
            return False
    except Exception as e:
        print(f"❌ Error reading app.py: {e}")
        return False
    
    # Check streamlit_app.py
    try:
        with open("streamlit_app.py", "r") as f:
            streamlit_content = f.read()
        if "import app" in streamlit_content and "app.main()" in streamlit_content:
            print("✅ streamlit_app.py entry point properly configured")
        else:
            print("❌ streamlit_app.py entry point issues")
            return False
    except Exception as e:
        print(f"❌ Error reading streamlit_app.py: {e}")
        return False
    
    return True

def check_documentation():
    """Check that documentation files are present and contain key information"""
    try:
        # Check README has initiative credit
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        if "Initiative Credit" in readme_content and "Mrs. Premlata Jain" in readme_content:
            print("✅ README.md contains initiative credit")
        else:
            print("❌ README.md missing initiative credit")
            return False
            
        # Check DEPLOYMENT.md mentions streamlit_app.py
        with open("DEPLOYMENT.md", "r", encoding="utf-8") as f:
            deploy_content = f.read()
        if "streamlit_app.py" in deploy_content:
            print("✅ DEPLOYMENT.md mentions streamlit_app.py")
        else:
            print("❌ DEPLOYMENT.md missing streamlit_app.py reference")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Error checking documentation: {e}")
        return False

def check_git_status():
    """Check that all necessary files are committed"""
    try:
        import subprocess
        result = subprocess.run(["git", "status", "--porcelain"], 
                              capture_output=True, text=True, cwd=".")
        if result.stdout.strip() == "":
            print("✅ All files committed to git")
            return True
        else:
            print("ℹ️  There are uncommitted changes (not necessarily an issue)")
            print("   Uncommitted files:")
            for line in result.stdout.strip().split('\n'):
                if line:
                    print(f"     {line}")
            return True  # This is not necessarily a failure
    except Exception as e:
        print(f"❌ Error checking git status: {e}")
        return False

def main():
    """Main verification function"""
    print("PWD Tools Hub Deployment Verification")
    print("=" * 40)
    
    checks = [
        ("Required Files", check_required_files),
        ("Streamlit Configuration", check_streamlit_config),
        ("Entry Points", check_entry_points),
        ("Documentation", check_documentation),
        ("Git Status", check_git_status)
    ]
    
    results = []
    for check_name, check_function in checks:
        print(f"\n[{check_name}]")
        result = check_function()
        results.append(result)
    
    print("\n" + "=" * 40)
    if all(results):
        print("✅ All deployment checks passed!")
        print("\nRepository is ready for Streamlit Cloud deployment.")
        print("To deploy:")
        print("  1. Go to https://streamlit.io/cloud")
        print("  2. Create new app")
        print("  3. Connect to CRAJKUMARSINGH/PWD-Tools-Genspark2 repository")
        print("  4. Select main branch")
        print("  5. Deploy!")
        return True
    else:
        print("❌ Some deployment checks failed!")
        print("Please review the issues above before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)