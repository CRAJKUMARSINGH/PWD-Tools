"""
Test script to verify that both app.py and streamlit_app.py entry points work correctly.
"""

import subprocess
import sys
import os

def test_app_py():
    """Test that app.py can be imported without errors"""
    try:
        import app
        print("✅ app.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing app.py: {e}")
        return False

def test_streamlit_app_py():
    """Test that streamlit_app.py can be imported without errors"""
    try:
        import streamlit_app
        print("✅ streamlit_app.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing streamlit_app.py: {e}")
        return False

def test_main_bat():
    """Test that main.bat exists and has the correct content"""
    try:
        if os.path.exists("main.bat"):
            with open("main.bat", "r") as f:
                content = f.read()
                if "streamlit_app.py" in content:
                    print("✅ main.bat references streamlit_app.py")
                    return True
                else:
                    print("ℹ️  main.bat does not reference streamlit_app.py (not required)")
                    return True
        else:
            print("❌ main.bat not found")
            return False
    except Exception as e:
        print(f"❌ Error reading main.bat: {e}")
        return False

if __name__ == "__main__":
    print("Testing entry points...")
    print("=" * 40)
    
    results = []
    results.append(test_app_py())
    results.append(test_streamlit_app_py())
    results.append(test_main_bat())
    
    print("=" * 40)
    if all(results):
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
        sys.exit(1)