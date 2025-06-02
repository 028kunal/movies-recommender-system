import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies =[]

    for i in movies_list:
        movie_id = i[0]
        # fetching poster from API call
        recommended_movies.append(movies.iloc[i[0]].title)
        print()
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Please Select the Movie',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)