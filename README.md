# 🎬 Movie Recommender System

Hi! I'm Ravish Kumar (Balister), and this is a project I built — a **Content-Based Movie Recommender System** using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. The app recommends similar movies based on user input by calculating cosine similarity between movie vectors derived from metadata like cast, genre, and overview.

## 🚀 Live App

👉 [Click here to try it out](https://balister-movie-recommender.streamlit.app/))

---

## 📌 What This App Does

- Suggests **top 5 similar movies** when you enter a movie name
- Displays posters of the recommended movies using **TMDB API**
- Built with **Streamlit** for simplicity and speed
- Fully deployed and shareable through a public link

## 🧠 How It Works (Brief Overview)

- I used a dataset of movies containing metadata like genres, cast, crew, etc.
- Processed and combined these features into a single **'tags'** column
- Vectorized the data using **CountVectorizer**
- Calculated **cosine similarity** between vectors
- Precomputed and saved the similarity matrix using `pickle`
- The app loads everything and returns recommendations instantly

## 📁 Project Structure

```
movie.recomender.system/
├── app.py                  # Main Streamlit script
├── movies_dic.pkl          # Movie metadata (ID, title, etc.)
├── similarity.pkl          # Precomputed cosine similarity matrix
├── requirements.txt        # Python dependencies
└── README.md               # You're here
```

---

## 🧰 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle (for saving models/data)
- TMDB API (for posters)

## 📦 requirements.txt

```
streamlit
pandas
scikit-learn
requests
```
## 🌐 How I Deployed It on Streamlit Cloud

1. I pushed the complete project to my GitHub repo.
2. Logged into [Streamlit Cloud](https://streamlit.io/cloud).
3. Clicked **“Deploy an app”**, selected the repo and `app.py`.
4. Shared the generated public link — super simple!

⭐ If you found this helpful, feel free to give it a star!
