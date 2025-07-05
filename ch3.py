import streamlit as st

st.title("Programming langauage poll")

col1, col2 = st.columns(2)
with col1:
    st.header("Python")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png", width=200)
    vote1 = st.button("Vote for Python", key="python_vote")

with col2:
    st.header("Java") 
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/640px-Java_programming_language_logo.svg.png", width = 200)
    vote2 = st.button("Vote for Java", key="java_vote")

st.write("Click on the buttons to vote for your favorite programming language")


st.header("Results")
if vote1:
    st.success("You voted for Python")
elif vote2:
    st.write("You voted for Java")
else:
    st.write("Please vote for your favorite programming language")
if st.button("Reset Votes"):
    st.write("Votes have been reset")
    st.rerun()  # This will reset the state of the app



name = st.sidebar.text_input("Enter you name : ")
env_choice = st.sidebar.selectbox("Choose your environment : ", ["Select you environment","pip", "uv", "IDLE", "jdk"])

if name:
    st.write(f"Welcome {name} to the streamlit app")
else:
    st.write(f"Welcome guest to the streamlit app")


if env_choice == "Select you environment":
    st.write("Please select your environment from the dropdown menu")
elif env_choice:  
    st.write(f"You have chosen {env_choice} as your environment")
else:
    st.write("Please select your environment from the dropdown menu")



st.title("This is the code from chai aud code :-")
import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/16228436/pexels-photo-16228436/free-photo-of-a-table-with-a-tea-pot-and-a-candle-on-it.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/29054033/pexels-photo-29054033/free-photo-of-elegant-overhead-view-of-tea-on-checkered-tablecloth.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "kesar", "Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("Show Chai Making INstructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
 """)
    
st.markdown('# Welcome to Chai App')
st.markdown('> Blockquote ')
