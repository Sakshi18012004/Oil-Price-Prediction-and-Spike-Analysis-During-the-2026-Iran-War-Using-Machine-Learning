import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Oil Price Prediction System")

# Inputs (ALL FEATURES)
wti = st.number_input("WTI Oil Price")
dubai = st.number_input("Dubai Oil Price")
gas = st.number_input("US Gas Price")
ships = st.number_input("Ships in Strait of Hormuz")
production = st.number_input("Iran Production (mbpd)")
war_day = st.number_input("War Day")

lag_price = st.number_input("Previous Day Price")
rolling_mean = st.number_input("Rolling Mean Price")

if st.button("Predict Price"):
    input_data = np.array([[wti, dubai, gas, ships, production, war_day, lag_price, rolling_mean]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Brent Price: {prediction[0]:.2f} USD/barrel")