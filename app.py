import streamlit as st
import pickle
import pandas as pd
import requests

# --- Function to fetch poster from TMDb by title ---
def fetch_poster_by_title(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': '8265bd1679663a7ea12ac168da84d2e8',
        'query': movie_title
    }
    response = requests.get(search_url, params=params)
    data = response.json()

    if data.get('results'):
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    # Return placeholder image if no poster found
    return "https://via.placeholder.com/500x750?text=No+Poster"

# --- Recommendation function ---
def recommend(movie_title):
    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_movies_posters.append(fetch_poster_by_title(title))
    return recommended_movies, recommended_movies_posters

# --- Load data ---
movies_dict = pickle.load(open("movies_dic.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# --- Streamlit UI ---
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie:', movies["title"].values)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
