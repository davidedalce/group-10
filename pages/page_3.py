import streamlit as st
import sys
import os
import subprocess
import altair as alt
import ollama

sys.path.append(os.path.abspath("models"))
from movie_analyzer import MovieAnalyzer  # Import from models/

# Initialize analyzer
analyzer = MovieAnalyzer()

# Initialize LLM
try:
    subprocess.run(["ollama", "pull", "llama3.2"], check=True)
except Exception as e:
    st.error(f"Failed to pull Ollama model: {e}")

st.title("CMU Movies Dataset")

# Shuffle button (fixed: removed icon parameter)
shuffle_button = st.button(label="Shuffle", use_container_width=True)

# Press button
if shuffle_button:
    analyzer.randomize()
    movie_name = analyzer.random_movie["movie_name"]
    movie_release_year = analyzer.random_movie["release_date"].year
    movie_genres = f'{", ".join(analyzer.random_movie["genres"])}'

    # Generate storyline (fixed: proper function call)
    storyline = ollama.generate(model='llama3.2', prompt=f"""You are requested to fetch the storyline/plot of a given 
                                movie based on your knowledge. Please respond with only the storyline or plot. If you 
                                cannot find it, please simply respond with 'No information'. 
                                \nThe movie is: {movie_name}, released in {movie_release_year}""")
    
    # Generate genres (fixed: proper function call)
    genres = ollama.generate(model='llama3.2', prompt=f"""In your response, you only need to suggest a series of genres 
                             based on a given movie (maximum 5) separated by commas. Text other than genre names is not 
                             requested. \nThe movie is: {movie_name}, released in {movie_release_year}""")

    # Evaluate classification result (fixed: correct response attribute)
    evaluation = ollama.generate(model='llama3.2', prompt=f"""Compare a classification result of genres: 
                                 {genres['response']} to CMU Movie Dataset: {movie_genres}, to see if genres appearing 
                                 in the first set are found in the second set.
                                 Response should follow this format without extra words: 
                                 'Found: <genres in set 1> \n Not Found: <genres not in set 1>'.
                                 \n You should strictly compare those words, do not try to guess if they point to the same genre!""")
    
    st.header(f"{movie_name} ({movie_release_year})", divider="red")

    st.write("### Summary")
    st.write("**Release Date:**", analyzer.random_movie["release_date"])
    st.write("**Languages:**", f'{", ".join(analyzer.random_movie["languages"])}')
    st.write("**Countries:**", f'{", ".join(analyzer.random_movie["countries"])}')
with st.chat_message(name="storyline", avatar="assistant"):
    st.text_area("Storyline suggested by AI", storyline['response'])

with st.chat_message(name="genres", avatar="user"):
    st.text_area("Genres from dataset", f'{", ".join(analyzer.random_movie["genres"])}')

with st.chat_message(name="genres", avatar="assistant"):
    st.text_area("Genres suggested by AI", genres['response'])
    st.text_area("Evaluation", evaluation['response'])
    
    
    
