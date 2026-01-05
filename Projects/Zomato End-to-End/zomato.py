# app.py
import streamlit as st
import pandas as pd
import joblib  # for loading your trained model
# Load your trained model (pipeline that includes preprocessing)
model = joblib.load(r"C:\Users\mikun\1. Full stack Data Science and AI\Projects\zomato_pipeline.pkl")  # replace with your actual file path

st.title("🍽️ Zomato Restaurant Rating Predictor")

st.markdown("""
Predict restaurant ratings based on features like cost, availability, type, and cuisines.
""")

# --- NUMERICAL INPUTS ---
st.header("Numerical Features")
cost_for_two = st.number_input("Cost for Two", min_value=0, value=500, step=50)
online_order = st.selectbox("Online Order Available?", options=[0, 1])
book_table = st.selectbox("Table Booking Available?", options=[0, 1])
votes = st.number_input("Number of Votes", min_value=0, value=50, step=1)
dish_available = st.selectbox("Dish Available?", options=[0, 1])

# --- CATEGORICAL INPUTS ---
st.header("Categorical Features")

listed_in_city = st.selectbox(
    "City",
    options=[
        "Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Kolkata", "Pune", "Other"
    ]
)

listed_in_type = st.selectbox(
    "Type of Listing",
    options=[
        "Delivery", "Dine-out", "Desserts", "Buffet", "Cafes", "Other"
    ]
)

rest_type = st.selectbox(
    "Restaurant Type",
    options=[
        "Casual Dining", "Cafe", "Quick Bites", "Bakery", "Bar", "Other"
    ]
)

cuisines = st.selectbox(
    "Cuisine",
    options=[
        "North Indian", "South Indian", "Chinese", "Fast Food", "Italian", "Continental", "Other"
    ]
)

# --- PREDICT BUTTON ---
if st.button("Predict Rating"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "cost_for_two": [cost_for_two],
        "online_order": [online_order],
        "book_table": [book_table],
        "votes": [votes],
        "dish_available": [dish_available],
        "listed_in(city)": [listed_in_city],
        "listed_in(type)": [listed_in_type],
        "rest_type": [rest_type],
        "cuisines": [cuisines]
    })

    # Make prediction
    prediction = model.predict(input_data)

    st.success(f"⭐ Predicted Rating: {prediction[0]:.2f}")
