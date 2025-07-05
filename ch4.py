import streamlit as st 
import pandas as pd

st.title("Chai sales Dashboard")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)


if file:
    st.subheader("Sales Summary")
    st.write(df.describe())

if file:
    ct = df["City"].unique()
    selected_city = st.selectbox("Select a city", ct)
    st.write(f"You selected: {selected_city}")
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)