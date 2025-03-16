import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("pages"))  # Ensure the "pages" directory is accessible

PAGES = {
    "Distribution Analysis": "./pages/page_1.py",
    "Chronological Analysis": "./pages/page_2.py",
    "I'm Feeling Lucky": "./pages/page_3.py"
}

st.sidebar.title("Movie Analyzer")  # Sidebar title
selection = st.sidebar.radio("Go to", list(PAGES.keys()))  # Sidebar navigation

# Dynamically load the selected page
if selection in PAGES:
    with open(PAGES[selection]) as f:
        exec(f.read())  # Execute the selected page

