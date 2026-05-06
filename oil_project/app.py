import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

#PAGE SETTINGS
st.set_page_config(
    page_title="Oil Price Prediction",
    page_icon="⛽",
    layout="centered"
)

#DARK THEME STYLE
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
h1, h2, h3 {
    color: #00FFAA;
}
.stButton>button {
    background-color: #00FFAA;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

#TITLE 
st.title("⛽ Oil Price Prediction During Iran War 2026")

st.write("""
This ML system predicts Brent crude oil prices 
based on war conditions and market trends.
""")

# COUNTRY DROPDOWN 
country = st.selectbox(
    "🌍 Select Country",
    ["India", "USA", "China", "UAE"]
)

#USER INPUT
barrels = st.number_input(
    "🛢 Enter Number of Barrels",
    min_value=1
)

# WAR INTENSITY
war_intensity = st.selectbox(
    "⚔ Select War Intensity",
    ["Low", "Medium", "High"]
)

#DEFAULT FEATURE VALUES
wti = 65
dubai = 66
gas = 2.8
ships = 140
production = 3.2
lag_price = 70
rolling_mean = 71

#WAR EFFECT
if war_intensity == "Low":
    war_day = 5

elif war_intensity == "Medium":
    war_day = 15

else:
    war_day = 30

#PREDICTION
if st.button("🚀 Predict Oil Price"):

    # Input array
    input_data = np.array([[
        wti,
        dubai,
        gas,
        ships,
        production,
        war_day,
        lag_price,
        rolling_mean
    ]])

    # Predict price
    price_per_barrel = model.predict(input_data)[0]

    # Total cost
    total_cost = price_per_barrel * barrels

    #OUTPUT
    st.success(f"✅ Predicted Brent Price: {price_per_barrel:.2f} USD/barrel")

    st.success(f"💰 Total Cost: {total_cost:.2f} USD")

    #SPIKE ALERT
    if price_per_barrel > 75:
        st.error("⚠ Oil Price Spike Detected!")

    else:
        st.info("✔ Market is Stable")

    #LIVE GRAPH
    st.subheader("📈 Predicted Oil Price Trend")

    prices = [
        price_per_barrel - 3,
        price_per_barrel - 1,
        price_per_barrel,
        price_per_barrel + 2
    ]

    days = ["Day 1", "Day 2", "Day 3", "Day 4"]

    df = pd.DataFrame({
        "Days": days,
        "Prices": prices
    })

    fig, ax = plt.subplots()

    ax.plot(df["Days"], df["Prices"], marker='o')

    ax.set_xlabel("Days")
    ax.set_ylabel("Oil Price")

    ax.set_title("Oil Price Trend")

    st.pyplot(fig)

#FOOTER
st.markdown("---")
st.write("Developed using Machine Learning + Streamlit")