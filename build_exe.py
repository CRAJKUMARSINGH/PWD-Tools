import PyInstaller.__main__
import platform

# Cross-platform build script
# On Windows: use --add-data=static;static
# On Linux/Mac: use --add-data=static:static

separator = ";" if platform.system() == "Windows" else ":"

PyInstaller.__main__.run([
    "main.py",
    "--name=PwdTools",
    "--noconsole",
    "--onefile",
    f"--add-data=static{separator}static",
    "--hidden-import=streamlit",
    "--collect-all=streamlit",
    "--collect-all=altair",
    "--collect-all=pandas",
    "--collect-all=numpy",
    "--collect-all=PIL",
    "--collect-all=PySide6",
])