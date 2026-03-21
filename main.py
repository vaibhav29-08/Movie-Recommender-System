import streamlit as st
import pickle


def recommend(movies):
    movie_index = movie_list[movie_list['title'] == movies].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]


    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movie_list.iloc[i[0]].title)




movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movie_list['title'].values
st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
'How Would You Like To Be Contacted?',
    movie_list)

st.button("Reset", type="primary")
if st.button("Recommend"):
    recommend(selected_movie_name)
    st.write(selected_movie_name)
else:
    st.write("Wrong Input")
