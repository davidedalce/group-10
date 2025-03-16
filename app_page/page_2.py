import streamlit as st
import sys
import os
import altair as alt

sys.path.append(os.path.abspath("models"))  # Ensure Python finds the models folder

from movie_analyzer import MovieAnalyzer  # Import from models/

def run():
    """Run the Streamlit page for Chronological Info."""
    
    #  Custom Styling
    st.markdown("""
        <style>
            h1, h2 { text-align: center; color: #32CD32; }
            .stButton>button { background-color: #4682B4; color: white; border-radius: 8px; }
            div[data-testid="stSelectbox"] select { border-radius: 6px; border: 2px solid #FF4500; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📆 CMU Movie Explorer - Chronological Analysis")

    analyzer = MovieAnalyzer()

    #  Movie Release Years
    st.header("🎬 Movie Releases Over Time", divider="green")

    genre_options = [None, 'Drama', 'Comedy', 'Romance Film', 'Black-and-white', 'Action', 
                     'Thriller', 'Short Film', 'World cinema', 'Crime Fiction', 'Indie']
    
    selected_genre = st.selectbox("🎭 Filter by Genre (Optional)", options=genre_options, index=0)

    chart_type = st.radio("📊 Choose Chart Type:", ["Bar Chart", "Line Chart"])

    movie_data = analyzer.releases(selected_genre)

    if chart_type == "Bar Chart":
        st.bar_chart(movie_data.set_index("Release Year"))
    else:
        st.line_chart(movie_data.set_index("Release Year"))

    #  Actor Birth Year & Month Distribution
    st.header("🎂 Actor Birth Trends", divider="green")

    selected_scale = st.radio("📆 Select Time Scale", ["Yearly Births", "Monthly Births"])

    if selected_scale == "Yearly Births":
        st.bar_chart(analyzer.ages("Y").set_index("Year"))
    else:
        c = alt.Chart(analyzer.ages("M")).mark_bar().encode(
            x=alt.X("Month", sort=None), y="Number of Births"
        )
        st.altair_chart(c, use_container_width=True)


#  Ensure the script runs independently & in `main.py`
if __name__ == "__main__":
    run()

