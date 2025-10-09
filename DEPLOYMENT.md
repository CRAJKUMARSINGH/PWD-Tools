# PWD Tools Hub Deployment Guide

This document provides comprehensive instructions for deploying the PWD Tools Hub application in various environments.

## 📚 Historical Context

The PWD Tools Hub has evolved through several deployment methods:

1. **Initial Deployment**: Used [run_app.bat](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\run_app.bat) with a simple `python app.py` command
2. **Enhanced Deployment**: Introduced [main.bat](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\main.bat) with better user experience
3. **Modern Deployment**: Uses proper Streamlit invocation with `python -m streamlit run app.py`

The current recommended approach is using the Streamlit module invocation for better compatibility and features.

## 🎯 Deployment Scenarios

### 1. Local Development
For developers working on the application locally.

### 2. Production Server
For deploying to a server accessible by multiple users.

### 3. Cloud Deployment
For deploying to cloud platforms like Streamlit Community Cloud, Heroku, etc.

## 🛠️ Prerequisites

### System Requirements
- Python 3.8 or higher
- 500MB free disk space
- 2GB RAM minimum (4GB recommended)

### Required Software
- Git (for cloning repository)
- Python and pip
- Virtual environment tool (optional but recommended)

## 📦 Installation Process

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd PWD-Tools-Genspark2
```

### Step 2: Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import streamlit; print('Streamlit version:', streamlit.__version__)"
```

## ▶️ Running the Application

### Development Mode
```bash
# Using the deployment script (recommended)
python deploy.py --mode dev

# Or directly with Streamlit (current recommended approach)
streamlit run app.py

# Using the main.bat launcher (Windows)
main.bat

# Direct Python execution (older method, still works)
python app.py
```

### Production Mode
```bash
# Using the deployment script
python deploy.py --mode prod

# Or directly with Streamlit
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

## ⚙️ Entry Points

The application supports multiple entry points for different deployment scenarios:

### 1. Local Development ([app.py](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\app.py))
- Used for local development with [main.bat](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\main.bat)
- Contains the main application logic
- Includes credits display when run directly

### 2. Streamlit Cloud Deployment ([streamlit_app.py](file://c:\Users\Rajkumar\PWD-Tools-Genspark2\venv\Lib\site-packages\streamlit\hello\streamlit_app.py))
- Used by Streamlit Community Cloud as the default entry point
- Simplified entry point that imports and runs the main application
- Can be specified when setting up the Streamlit Cloud deployment

To deploy to Streamlit Cloud:
1. Push your code to GitHub
2. Create a new app on Streamlit Community Cloud
3. Point it to your repository
4. Set `streamlit_app.py` as the main file (optional, as it's the default)

## ⚙️ Configuration

### Streamlit Configuration
Located at `.streamlit/config.toml`:
```toml
[server]
port = 8501
address = "0.0.0.0"
enableCORS = false
enableXsrfProtection = false

[theme]
base = "light"
primaryColor = "#2E8B57"
```

### Application Configuration
Located at `config.toml`:
```toml
[server]
port = 5000
address = "127.0.0.1"
```

## ☁️ Cloud Deployment

### Streamlit Community Cloud
1. Push your code to GitHub
2. Create a new app on Streamlit Community Cloud
3. Point it to your repository
4. Set `app.py` as the main file

### Heroku Deployment
1. Create a `Procfile`:
   ```
   web: streamlit run app.py
   ```

2. Create a `runtime.txt`:
   ```
   python-3.11.9
   ```

3. Deploy using Heroku CLI:
   ```bash
   heroku create
   git push heroku main
   ```

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t pwd-tools .
docker run -p 8501:8501 pwd-tools
```

## 🔧 Maintenance

### Updating the Application
```bash
# Pull latest changes
git pull

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Monitoring
- Check server logs for errors
- Monitor resource usage
- Set up health checks

### Backup
- Regularly backup the repository
- Backup any persistent data (if applicable)

## 🔒 Security Considerations

### Network Security
- Use HTTPS in production
- Restrict access to authorized users
- Implement authentication if needed

### Application Security
- Keep dependencies updated
- Validate all user inputs
- Sanitize file uploads

### Server Security
- Run the application with minimal privileges
- Use firewalls to restrict access
- Regularly update the OS

## 📈 Performance Optimization

### Caching
The application uses Streamlit's built-in caching mechanisms for better performance.

### Resource Management
- Monitor memory usage
- Optimize large data processing
- Use efficient data structures

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **Port Already in Use**
   ```bash
   # Kill process using port 8501
   # On Windows:
   netstat -ano | findstr :8501
   taskkill /PID <PID> /F
   ```

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission Errors**
   - Run as administrator (Windows)
   - Check file permissions (Linux/macOS)

4. **Import Errors**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:."
   ```

### Logs and Debugging
```bash
# Enable debug mode
streamlit run app.py --logger.level=debug
```

## 🔄 CI/CD Integration

### GitHub Actions Example
```yaml
name: Deploy PWD Tools
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python comprehensive_test.py
```

## 📊 Monitoring and Analytics

### Built-in Streamlit Metrics
- Session count
- User interactions
- Performance metrics

### Custom Monitoring
Implement custom logging for:
- Tool usage statistics
- Error tracking
- Performance benchmarks

## 📞 Support

For deployment issues or questions:
1. Check the logs for error messages
2. Refer to this documentation
3. Contact the development team