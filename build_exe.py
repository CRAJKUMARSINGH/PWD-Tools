import PyInstaller.__main__

PyInstaller.__main__.run([
    "main.py",
    "--name=PwdTools",
    "--noconsole",
    "--onefile",
    "--add-data=static;static",
    "--hidden-import=streamlit",
    "--collect-all=streamlit",
    "--collect-all=altair",
    "--collect-all=pandas",
    "--collect-all=numpy",
    "--collect-all=PIL",
    "--collect-all=PySide6",
])