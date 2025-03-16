# group-10
The repository for ADPRO group project (Group 10)

STUDENTS:
- Davide Dal Cero (64018@novasbe.pt)
- Pietro Ghiotto (68096@novasbe.pt)
- Rohit Hassan (67724@novasbe.pt)
- Laura Volpe (68106@novasbe.pt)

The application consists of:

-A Python class (MovieAnalyzer) to process and analyze movie data.
-A Streamlit web app with three pages for data visualization and classification.
-Integration with a local LLM (Ollama) to classify movie genres.

How to run the project:

**STEP 1**: Clone the repository:
git clone https://github.com/davidedalce/group-10.git
cd group-10

**STEP 2**: Install dependencies:
pip install -r requirements.txt

**STEP 3**: Run the Streamlit App:
streamlit run main.py

### **Summary of the Streamlit App**
PAGE 1: Analyzes and visualizes movie genres; Shows the number of actors per movie; Displays actor height distribution; interactive controls allow users to filter the data.

PAGE 2: Visualizes the number of movie releases per year; Shows actor birth trends (by year or month); Users can select specific genres for movie releases.

PAGE 3: Randomly selects a movie from the dataset; Uses Ollama's Llama3.2 LLM to predict genres; Compares AI-predicted genres with the dataset; Shows an evaluation of AI accuracy.
