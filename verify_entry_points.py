"""
Verification script to test both app.py and streamlit_app.py entry points.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_app_py_import():
    """Test importing app.py"""
    try:
        import app
        print("✅ app.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import app.py: {e}")
        return False

def test_streamlit_app_py_import():
    """Test importing streamlit_app.py"""
    try:
        import streamlit_app
        print("✅ streamlit_app.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import streamlit_app.py: {e}")
        return False

def verify_files_exist():
    """Verify that both files exist"""
    files_to_check = ["app.py", "streamlit_app.py"]
    all_exist = True
    
    for file_name in files_to_check:
        if os.path.exists(file_name):
            print(f"✅ {file_name} exists")
        else:
            print(f"❌ {file_name} not found")
            all_exist = False
    
    return all_exist

def check_streamlit_app_content():
    """Check that streamlit_app.py has the correct content"""
    try:
        with open("streamlit_app.py", "r") as f:
            content = f.read()
            
        if "import app" in content and "app.main()" in content:
            print("✅ streamlit_app.py has correct content")
            return True
        else:
            print("❌ streamlit_app.py content is incorrect")
            return False
    except Exception as e:
        print(f"❌ Error reading streamlit_app.py: {e}")
        return False

if __name__ == "__main__":
    print("Verifying entry points...")
    print("=" * 40)
    
    results = []
    results.append(verify_files_exist())
    results.append(test_app_py_import())
    results.append(test_streamlit_app_py_import())
    results.append(check_streamlit_app_content())
    
    print("=" * 40)
    if all(results):
        print("✅ All verifications passed!")
        print("\nEntry points are ready for deployment:")
        print("  - Local development: app.py (used by main.bat)")
        print("  - Streamlit Cloud: streamlit_app.py")
    else:
        print("❌ Some verifications failed!")
        sys.exit(1)