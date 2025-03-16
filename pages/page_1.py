import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("models"))  # Ensure Python finds the models folder

from movie_analyzer import MovieAnalyzer  # Import from models/


def run():
    """Run the Streamlit page for Movie Type Distribution and Actor Statistics."""
    
    # 🎨 Custom Styling for Uniqueness
    st.markdown("""
        <style>
            h1, h2 { text-align: center; color: #FF8C00; }
            .stButton>button { background-color: #8A2BE2; color: white; border-radius: 8px; }
            .stNumberInput input { border-radius: 6px; border: 2px solid #FFA07A; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🍿 CMU Movies Explorer - Distribution Analysis")

    analyzer = MovieAnalyzer()

    # 📊 Movie Type Distribution
    st.header("🎭 Movie Type Distribution", divider="blue")
    N = st.number_input("🎬 Select N", min_value=1, max_value=50, value=10)
    st.bar_chart(analyzer.movie_type(N).set_index("Movie_Type"))

    # 📊 Actor Count Histogram
    st.header("🎭 Actor Count Histogram", divider="blue")
    st.bar_chart(analyzer.actor_count().set_index("Number_of_Actors"))

    # 📊 Actor Height Distribution
    st.header("📏 Actor Height Distribution", divider="blue")
    gender = st.selectbox("👤 Select Gender", ["All", "Male", "Female"])
    min_height = st.number_input("📏 Min Height", min_value=0.5, max_value=2.5, value=1.0)
    max_height = st.number_input("📏 Max Height", min_value=0.5, max_value=2.5, value=2.5)
    
    # 🟣 Button with different style
    if st.button("🔄 Plot Distribution", use_container_width=True):
        analyzer.actor_distributions(gender, max_height, min_height, plot=True)


# ✅ Ensure the script runs independently & in `main.py`
if __name__ == "__main__":
    run()
