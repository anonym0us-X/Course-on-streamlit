import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Age calculator in streamlit")

st.subheader("Welcome to the age calculator app")

todays_date = st.date_input("Enter today's date")
birth_date = st.text_input("Enter your birth date (YYYY-MM-DD):")

if birth_date:
    try:
        # Convert to datetime.date to match todays_date
        birth_date = pd.to_datetime(birth_date).date()
        age = (todays_date - birth_date).days // 365
        st.write(f"Your age is: {age} years")
    except ValueError:
        st.error("Please enter a valid date in the format YYYY-MM-DD")
    
st.success("You have successfully calculated your age using streamlit")
