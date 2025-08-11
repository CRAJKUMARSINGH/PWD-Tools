import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons"""
    
    # Tool definitions with categories and external links
    tools = [
        {
            "name": "Excel se EMD",
            "description": "Hand Receipt Generator from Excel files",
            "icon": "📊",
            "category": "financial",
            "status": "internal",
            "url": None,
            "page": "pages/01_Excel_se_EMD.py"
        },
        {
            "name": "Bill & Deviation",
            "description": "Infrastructure Billing System with deviation tracking",
            "icon": "💰",
            "category": "financial", 
            "status": "external",
            "url": "https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/",
            "page": "pages/02_Bill_Deviation.py"
        },
        {
            "name": "Tender Processing",
            "description": "Comprehensive tender management system",
            "icon": "📋",
            "category": "processing",
            "status": "external", 
            "url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/",
            "page": "pages/03_Tender_Processing.py"
        },
        {
            "name": "Bill Note Sheet",
            "description": "Bill Note Sheet Generator for PWD documentation",
            "icon": "📝",
            "category": "processing",
            "status": "internal",
            "url": None,
            "page": "pages/04_Bill_Note_Sheet.py"
        },
        {
            "name": "Deductions Table", 
            "description": "Calculate all standard deductions for bill amounts",
            "icon": "📊",
            "category": "financial",
            "status": "internal",
            "url": None,
            "page": "pages/05_Deductions_Table.py"
        },
        {
            "name": "Delay Calculator",
            "description": "Calculate project delays and timeline analysis",
            "icon": "⏰",
            "category": "monitoring",
            "status": "internal", 
            "url": None,
            "page": "pages/06_Delay_Calculator.py"
        },
        {
            "name": "EMD Refund",
            "description": "Generate EMD refund receipts and documentation",
            "icon": "💰",
            "category": "financial",
            "status": "internal",
            "url": None,
            "page": "pages/07_EMD_Refund.py"
        },
        {
            "name": "Financial Progress",
            "description": "Track financial progress and liquidity damages",
            "icon": "📈",
            "category": "monitoring",
            "status": "internal",
            "url": None,
            "page": "pages/08_Financial_Progress.py"
        },
        {
            "name": "Security Refund",
            "description": "Process security deposit refund calculations",
            "icon": "🔒", 
            "category": "financial",
            "status": "internal",
            "url": None,
            "page": "pages/09_Security_Refund.py"
        },
        {
            "name": "Stamp Duty",
            "description": "Calculate stamp duty for work orders",
            "icon": "📋",
            "category": "financial",
            "status": "internal",
            "url": None,
            "page": "pages/10_Stamp_Duty.py"
        }
    ]
    
    colors = get_tool_colors()
    
    # Create simplified grid layout (2 rows of 5 tools each)
    for row in range(2):
        cols = st.columns(5)
        for col_idx, col in enumerate(cols):
            tool_idx = row * 5 + col_idx
            if tool_idx < len(tools):
                tool = tools[tool_idx]
                with col:
                    create_tool_button(tool, colors)

def create_tool_button(tool, colors):
    """Create individual tool button with proper styling"""
    
    category_color = colors.get(tool["category"], colors["operations"])
    status_indicator = "🔗" if tool["status"] == "external" else "🏠"
    
    # Create simple button container
    button_html = f"""
    <div class="tool-button" style="
        background: {category_color['bg']};
        border: 2px solid {category_color['border']};
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        min-height: 120px;
    ">
        <div style="font-size: 2.5rem; margin-bottom: 8px;">{tool['icon']}</div>
        <div style="font-size: 1rem; font-weight: bold; color: {category_color['border']};">
            {tool['name']} {status_indicator}
        </div>
    </div>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    
    # Navigation link (removes extra button clutter)
    st.page_link(tool["page"], label=f"Open {tool['name']}")

def create_category_filter():
    """Create category filter for tools"""
    st.sidebar.markdown("### 🎯 Filter by Category")
    
    categories = ["All", "Financial", "Processing", "Operations", "Monitoring"]
    selected_category = st.sidebar.selectbox("Select Category:", categories)
    
    return selected_category.lower() if selected_category != "All" else None

def show_tool_stats():
    """Display statistics about available tools"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔗 External Tools", "2", "Connected")
    with col2:
        st.metric("🏠 Internal Tools", "8", "Available")
    with col3:
        st.metric("📊 Total Categories", "4", "Organized")
