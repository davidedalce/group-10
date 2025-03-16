import streamlit as st
import sys
import os
import subprocess
import ollama
import time

sys.path.append(os.path.abspath("models"))
from movie_analyzer import MovieAnalyzer  # Import from models/

def run():
    """Run the Streamlit page for AI-based Genre Classification."""
    
    # 🎨 Custom Styling
    st.markdown("""
        <style>
            h1, h2 { text-align: center; color: #FF4500; }
            .stButton>button { background-color: #6A5ACD; color: white; border-radius: 8px; }
            div[data-testid="stChatMessage"] { background-color: #2E8B57; padding: 10px; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

    # Initialize analyzer
    analyzer = MovieAnalyzer()

    # Initialize LLM
    try:
        subprocess.run(["ollama", "pull", "llama3.2"], check=True)
    except Exception as e:
        st.error(f"⚠️ Failed to pull Ollama model: {e}")
        return

    st.title("🎲 AI-Powered Genre Classifier")

    # 📌 Shuffle Button with Cooldown
    if "last_click" not in st.session_state:
        st.session_state.last_click = 0

    if st.button("🔀 Shuffle Movie", use_container_width=True):
        if (st.session_state.last_click + 3) < time.time():
            st.session_state.last_click = time.time()
            with st.spinner("🔄 Selecting a random movie..."):
                analyzer.randomize()
            movie_name = analyzer.random_movie["movie_name"]
            movie_release_year = analyzer.random_movie["release_date"].year
            movie_genres = f'{", ".join(analyzer.random_movie["genres"])}'

            # 🎭 Generate storyline
            with st.spinner("🤖 Fetching AI-generated storyline..."):
                storyline = ollama.generate(model='llama3.2', prompt=f"""You are requested to fetch the storyline/plot 
                                    of a given movie based on your knowledge. Respond with only the storyline. If not 
                                    found, reply 'No information'. \nThe movie is: {movie_name}, released in {movie_release_year}""")

            # 🎭 Generate genres
            with st.spinner("📊 Classifying movie genres..."):
                genres = ollama.generate(model='llama3.2', prompt=f"""Suggest up to 5 genres based on a given movie, 
                                separated by commas. Respond only with genre names. \nThe movie is: {movie_name}, 
                                released in {movie_release_year}""")

            # 🧐 Evaluate classification result
            with st.spinner("✅ Verifying classification accuracy..."):
                evaluation = ollama.generate(model='llama3.2', prompt=f"""Compare classified genres {genres['response']} 
                                    to CMU Movie Dataset {movie_genres}. Respond in this format: 
                                    'Found: <matching genres> \n Not Found: <genres not matching>'.""")

            # 🎬 Display Results
            st.header(f"🎬 {movie_name} ({movie_release_year})", divider="blue")

            st.write("### Movie Summary")
            st.write("📅 **Release Date:**", analyzer.random_movie["release_date"])
            st.write("🗣 **Languages:**", f'{", ".join(analyzer.random_movie["languages"])}')
            st.write("🌍 **Countries:**", f'{", ".join(analyzer.random_movie["countries"])}')

            # Storyline
            with st.expander("📖 AI-Generated Storyline"):
                st.info(storyline['response'])

            # Genres from Database
            with st.expander("🎭 Genres (Database)"):
                st.success(f'{", ".join(analyzer.random_movie["genres"])}')

            # AI-Suggested Genres
            with st.expander("🤖 AI-Predicted Genres"):
                st.warning(genres['response'])

            # 🧐 AI vs Database Evaluation (Updated)
            st.subheader("🧐 AI vs Database Evaluation")

            evaluation_text = evaluation['response']

            # Extract found/not found genres properly
            found_genres = []
            not_found_genres = []

            if "Found:" in evaluation_text:
                found_part = evaluation_text.split("Found:")[1].split("\n")[0].strip()
                found_genres = [genre.strip() for genre in found_part.split(",") if genre]

            if "Not Found:" in evaluation_text:
                not_found_part = evaluation_text.split("Not Found:")[1].strip()
                not_found_genres = [genre.strip() for genre in not_found_part.split(",") if genre]

            # Display in a clearer way
            with st.expander("🔍 AI vs Database Evaluation Results"):
                st.markdown("### ✅ Matched Genres")
                if found_genres:
                    st.success(", ".join(found_genres))
                else:
                    st.warning("No matches found.")

                st.markdown("### ❌ AI-Predicted Genres NOT in Database")
                if not_found_genres:
                    st.error(", ".join(not_found_genres))
                else:
                    st.success("🎉 AI's predictions fully matched the database genres!")

        else:
            st.warning("🛑 Please wait a few seconds before shuffling again!")

# ✅ Ensure the script runs independently & in `main.py`
if __name__ == "__main__":
    run()


    
    
    
