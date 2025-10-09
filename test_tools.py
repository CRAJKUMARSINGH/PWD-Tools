import os
import webbrowser
import time

def test_html_tools():
    """Test all HTML tools by opening them in the browser"""
    html_dir = "static/html"
    html_files = [
        "EmdRefund.html",
        "BillNoteSheet.html",
        "DeductionsTable.html",
        "FinancialProgressTracker.html",
        "SecurityRefund.html",
        "StampDuty.html"
    ]
    
    print("Testing HTML tools...")
    for html_file in html_files:
        file_path = os.path.join(html_dir, html_file)
        if os.path.exists(file_path):
            full_path = os.path.abspath(file_path)
            print(f"Opening {html_file}...")
            webbrowser.open(f"file://{full_path}")
            time.sleep(2)  # Wait 2 seconds between opening files
        else:
            print(f"File not found: {file_path}")
    
    print("HTML tools test completed.")

def test_python_tools():
    """Test Python-based tools"""
    print("Testing Python-based tools...")
    # This would require running the Streamlit app, but we can at least check if files exist
    python_files = [
        "app.py",
        "components/tool_buttons.py",
        "utils/branding.py",
        "utils/navigation.py"
    ]
    
    for py_file in python_files:
        if os.path.exists(py_file):
            print(f"Found Python file: {py_file}")
        else:
            print(f"Missing Python file: {py_file}")
    
    print("Python tools check completed.")

if __name__ == "__main__":
    test_html_tools()
    test_python_tools()
    print("All tests completed.")