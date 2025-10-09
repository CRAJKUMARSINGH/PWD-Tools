import webbrowser
import os

# Open the updated EMD Refund HTML file in the default browser
html_file_path = os.path.abspath("static/html/EmdRefund.html")
webbrowser.open(f"file://{html_file_path}")
print(f"Opened updated {html_file_path} in your default browser")