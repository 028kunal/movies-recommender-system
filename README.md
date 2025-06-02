# movie-recommender-system
# 🎬 Movie Recommender System

This is a machine learning-based movie recommender system that suggests movies to users based on content similarity. The project utilizes natural language processing, vectorization, and similarity metrics to identify and recommend similar movies.

## 💡 Features

- Suggests similar movies based on user-selected input
- Combines movie metadata like genres, cast, crew, and tags
- Uses cosine similarity to measure movie similarity
- Integrated movie posters using The Movie Database (TMDb) API
- Built interactive frontend using Streamlit
- Deployed as a web application for real-time usage

## 🛠 Tech Stack

| Area              | Tools & Technologies                 |
|-------------------|--------------------------------------|
| Language          | Python                               |
| Libraries         | pandas, numpy, scikit-learn, requests, ast |
| NLP               | CountVectorizer (for text vectorization) |
| Web Framework     | Streamlit                            |
| Deployment        | Streamlit Cloud                      |
| External API      | TMDb API                             |
| Version Control   | Git & GitHub                         |

## 📁 Project Structure
├── app.py # Streamlit application
├── movies.csv # Dataset
├── similarity.pkl # Serialized similarity matrix
├── tmdb API integration # To fetch movie posters
├── vectorization & NLP # Text-based content similarity


## 🚀 How It Works

1. **Data Cleaning & Preprocessing**  
   Merged and cleaned movie metadata including genres, keywords, cast, and crew.

2. **Vectorization**  
   Transformed text data into numeric vectors using `CountVectorizer`.

3. **Similarity Calculation**  
   Used cosine similarity to find the most similar movies based on vector distance.

4. **Frontend with Streamlit**  
   Created a responsive UI that lets users select a movie and get recommendations with posters.

5. **API Integration**  
   Movie posters are fetched using TMDb API.

## 🖼 Sample UI

The user selects a movie title, and the app displays 5 similar movie titles along with their posters.



