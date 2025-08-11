import streamlit as st
import time
from utils.branding import apply_custom_css, show_header, show_credits, show_balloons
from components.tool_buttons import create_tool_grid

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and branding
apply_custom_css()

# Show header with branding
show_header()

# Main content area
def main():
    # Welcome section
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    
    # Create the main tool grid
    create_tool_grid()
    



# Main app execution
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()
    

