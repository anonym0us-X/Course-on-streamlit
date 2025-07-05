import streamlit as st 
import pandas as pd
import numpy as np 


st.set_page_config(page_title="Moviezzz",page_icon="🎞️",layout="wide", initial_sidebar_state="collapsed")

# st.set_page_config(
#      page_title="Ex-stream-ly Cool App",
#      page_icon="🧊",
#      layout="wide",
#      initial_sidebar_state="expanded",
#      menu_items={
#          'Get Help': 'https://www.extremelycoolapp.com/help',
#          'Report a bug': "https://www.extremelycoolapp.com/bug",
#          'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )

st.title("Lets make a movie recomendation")
st.subheader("You choose, I suggest")

st.write("This is a simple app to suggest movies based on your preferences")
st.write("Select your preferences in the sidebar to get recomendations")

# Sidebar for the selection process

st.sidebar.header("Movie Preferences")
st.sidebar.write("Select your preferences below to get started")
genre = st.sidebar.selectbox("Genre", ["Action", "Comedy", "Rom Com", "Drama", "Horror", "Romance"], index=None, placeholder="Select genre",)
lang = st.sidebar.selectbox("Language", ["English", "Hindi", "Tamil", "Telugu", "Kannada"], index= None,placeholder="Select the language" )
yr = st.sidebar.selectbox("Release Year", ["2020", "2021", "2022", "2023"], index=None,placeholder="Select the year")
rating = st.sidebar.selectbox("Rating", ["1", "2", "3", "4", "5"], index = None, placeholder="Select the rating")
st.sidebar.button("Get Recommendations")



#main screen content return
if (genre and lang and yr):
    st.write(f"You have choose {genre} with {lang} language and the year you have choosen is : {yr} ")



