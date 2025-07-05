import streamlit as st 
import requests

st.title("live Currency Converter")
amt = st.number_input("Enter amount in INR", min_value=0)

st.selectbox("Select currency", ["Select destination currency","USD", "EUR", "GBP", "JPY"])
if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        selected_currency = st.session_state.get("currency", "USD")
        if selected_currency in rates:
            converted_amount = amt * rates[selected_currency]
            st.success(f"{amt} INR is equal to {converted_amount:.2f} {selected_currency}")
        else:
            st.error("Selected currency not available.")