import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
   url = "https://api.themoviedb.org/3/movie/{}?api_key=2b712964f7255035fd47e2b0b93db897&language=en-US".format(
      movie_id)
   data = requests.get(url)
   data = data.json()
   poster_path = data['poster_path']
   full_path = "https://image.tmdb.org/t/p/w185/" + poster_path
   return full_path


def Recommend(movie):
   index = movies[movies['title'] == movie].index[0]
   movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
   recom_movie=[]
   recom_movie_poster=[]
   for i in movies_list[1:6]:
      #movie_id=i[0]
      movie_id = movies.iloc[i[0]].id
      recom_movie_poster.append(fetch_poster(movie_id))
      recom_movie.append(movies.iloc[i[0]].title)
   return recom_movie,recom_movie_poster

movie_dict= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
option = st.selectbox('List of movies', movies['title'].values)
if st.button('Recommend'):
   names,posters=Recommend(option)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
      st.text(names[0])
      st.image(posters[0])
   with col2:
      st.text(names[1])
      st.image(posters[1])

   with col3:
      st.text(names[2])
      st.image(posters[2])
   with col4:
      st.text(names[3])
      st.image(posters[3])
   with col5:
      st.text(names[4])
      st.image(posters[4])