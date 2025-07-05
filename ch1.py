import streamlit as st

st.title("Hello World App")
st.subheader("Welcome bhai log this is made by using streamlit")
st.text("My first interacvtive app using streamlit")

st.write("Choose ur fav language")


choice = st.selectbox("Select your language", ["Python", "Java", "C++", "JavaScript"])

if choice == "Java":
    st.write("Java mat le bhai gandi language hai")
elif choice == "Python":
    st.write(f"{choice} excellent choice hai bhai")

st.success("You have successfully created your first app using streamlit")