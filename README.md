# PWD Tools Hub

A comprehensive suite of infrastructure management tools for Public Works Department (PWD) operations.

## 🏗️ Project Overview

This application provides a collection of specialized tools for PWD operations including:
- EMD Refund Calculator
- Bill Deviation Tracker
- Tender Processing System
- Financial Progress Tracker
- And many more utilities

**Initiative Credit:**
_Mrs. Premlata Jain_
_Additional Administrative Officer, PWD Udaipur_
_Version 2.0 | Last Updated: September 2025_

## 📚 Historical Context

For information about how deployment methods have evolved and how to migrate between them, see [MIGRATION.md](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\MIGRATION.md).

## 🚀 Deployment Options

### Local Development Deployment

1. **Prerequisites**:
   - Python 3.8 or higher
   - pip package manager

2. **Installation**:
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd PWD-Tools-Genspark2
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   # Option 1: Using the deployment script (recommended)
   python deploy.py --mode dev
   
   # Option 2: Direct Streamlit command
   streamlit run app.py
   
   # Option 3: Using batch file (Windows)
   main.bat
   
   # Option 4: Direct Python execution (legacy)
   python app.py
   ```

### Production Deployment

For production deployment, use the deployment script with production mode:

```bash
python deploy.py --mode prod
```

### Creating Deployment Package

To create a deployment package for distribution:

```bash
python deploy.py --mode package
```

## ⚙️ Configuration

### Streamlit Configuration
The application uses `.streamlit/config.toml` for Streamlit-specific settings:
- Server port: 8501
- Address: 0.0.0.0 (for production)
- CORS disabled for local development
- Light theme with custom colors

### Application Configuration
The `config.toml` file contains server settings:
- Port: 5000 (alternative)
- Address: 127.0.0.1
- Security settings

## 📁 Project Structure

```
PWD-Tools-Genspark2/
├── app.py                 # Main application entry point
├── deploy.py              # Deployment script
├── main.bat               # Windows batch launcher
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python runtime version
├── config.toml            # Server configuration
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── pages/                 # Individual tool pages
├── components/            # UI components
├── utils/                 # Utility functions
└── static/                # Static assets (HTML, CSS, JS)
```

## 🛠️ Maintenance Protocol

### Regular Updates
1. Update dependencies:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. Check for Streamlit updates:
   ```bash
   pip install streamlit --upgrade
   ```

### Adding New Tools
1. Create a new page in the `pages/` directory
2. Add the tool to the `tools` list in `components/tool_buttons.py`
3. Update the tool count in `show_tool_stats()` function

### Testing
Run the comprehensive test suite:
```bash
python comprehensive_test.py
```

## 🌐 Accessing the Application

After starting the application, access it through your web browser:
- Development: http://localhost:8501
- Production: http://your-server-ip:8501

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change port in `.streamlit/config.toml`
   - Or kill the existing process using that port

2. **Missing dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission errors** (Windows):
   - Run as administrator
   - Or use the [main.bat](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\main.bat) script

### Python Path Issues
If you encounter import errors:
```bash
# Add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:."
# or on Windows
set PYTHONPATH=%PYTHONPATH%;.
```

## 📈 Performance Considerations

- The application is optimized for local network deployment
- For large deployments, consider using a reverse proxy (nginx)
- Static assets are served directly for better performance

## 🔒 Security Notes

- CORS is disabled for local development
- XSRF protection settings are configured
- File upload size is limited to 200MB

## 📞 Support

For issues or questions, please contact the development team.