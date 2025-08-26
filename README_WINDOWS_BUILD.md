# Windows EXE Build Guide

## What You'll Get
- **Single file**: `PwdTools.exe` (~150-250 MB)
- **No installation required** - just double-click to run
- **All PWD tools embedded** - Streamlit hub + any static sites
- **Offline capable** - no internet required after launch

## Prerequisites
- Windows 10/11 (64-bit)
- Python 3.9+ installed
- Git (optional, for cloning)

## Step-by-Step Build

### 1. Get the Code
```cmd
git clone <your-repo-url>
cd pwd-tools-desktop
```

### 2. Create Virtual Environment
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```cmd
pip install -r requirements.txt
```

### 4. Build the EXE
```cmd
python build_exe.py
```

### 5. Find Your EXE
The executable will be in `dist\PwdTools.exe`

## What Happens When You Run It
1. **Double-click** `PwdTools.exe`
2. **Main window opens** with tabs
3. **Tab 1**: PWD Tools Hub (Streamlit app)
4. **Tab 2+**: Any static HTML/JS tools you add
5. **All tools work offline** - no sleeping containers!

## Troubleshooting
- **"Missing DLL" errors**: Install Visual C++ Redistributable
- **"Windows Defender blocked"**: Click "More info" → "Run anyway"
- **"SmartScreen warning"**: Click "More info" → "Run anyway"

## Distribution
- **Single file**: Just give users `PwdTools.exe`
- **Portable**: Users can put it anywhere, no install needed
- **Self-contained**: Includes Python + Qt + all dependencies

## File Size Breakdown
- **Python runtime**: ~30 MB
- **Qt + WebEngine**: ~120 MB  
- **Streamlit + pandas**: ~50 MB
- **Your tools**: ~10-20 MB
- **Total**: ~150-250 MB

## Why This Approach?
- ✅ **No sleeping containers** - always available
- ✅ **No internet required** after launch
- ✅ **Single executable** - easy distribution
- ✅ **Native performance** - Qt is fast
- ✅ **Cross-platform** - same code works on Mac/Linux too