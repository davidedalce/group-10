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

# 📌 Navigation (ONLY Keep This)
st.sidebar.markdown("## 🎬 Navigation")
selected_page = st.sidebar.radio("Choose a Page:", ["Distribution Analysis", "Chronological Info", "Genre Classification"])

# 🚀 Load the selected page
if selected_page == "Distribution Analysis":
    with open("./pages/page_1.py") as f:
        exec(f.read())
elif selected_page == "Chronological Info":
    with open("./pages/page_2.py") as f:
        exec(f.read())
elif selected_page == "Genre Classification":
    with open("./pages/page_3.py") as f:
        exec(f.read())
# 🔄 Reload the module (useful if files are modified)
importlib.reload(module)

# Run the page
module.run()
