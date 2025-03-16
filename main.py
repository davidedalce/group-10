import streamlit as st
import importlib
import sys
import os

# Ensure Streamlit finds the pages directory
sys.path.append(os.path.abspath("pages"))

# 🏆 Custom Styling
st.markdown("""
    <style>
        h1 { text-align: center; color: #FFA500; }
        div[data-testid="stSidebar"] { background-color: #2A2A2A; }
        [data-baseweb="button"] { background-color: #FF6347 !important; color: white !important; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 🎬 App Title
st.title("🎬 CMU Movie Explorer")

# 📌 Sidebar Navigation
st.sidebar.markdown("## 🎬 Navigation")
selected_page = st.sidebar.radio(
    "Choose a Page:", 
    ["Distribution Analysis", "Chronological Info", "Genre Classification"]
)

# ✅ Dynamically Import the Selected Page
if selected_page == "Distribution Analysis":
    module = importlib.import_module("pages.page_1")
elif selected_page == "Chronological Info":
    module = importlib.import_module("pages.page_2")
elif selected_page == "Genre Classification":
    module = importlib.import_module("pages.page_3")

# 🔄 Reload the module (useful if files are modified)
importlib.reload(module)

# Run the page
module.run()
