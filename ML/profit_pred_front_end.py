import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"D:\Mikun\All Learnings\Data Science Spyder\profit_prediction.pkl", "rb"))
columns = pickle.load(open(r"D:\Mikun\All Learnings\Data Science Spyder\profit_pred_cols.pkl", "rb"))

st.title("Startup Profit Prediction")

col1, col2, col3 = st.columns(3)
with col1:
    digital = st.number_input("Digital Marketing Spend", min_value=0)
with col2:
    research = st.number_input("Research Spend", min_value=0)
with col3:
    promotion = st.number_input("Promotion Spend", min_value=0)

state = st.selectbox("State", ["Bangalore", "Chennai", "Hyderabad"])

if st.button("Predict Profit"):
    data = dict.fromkeys(columns, 0)

    # Fill numeric inputs
    data['DigitalMarketing'] = digital
    data['Research'] = research
    data['Promotion'] = promotion

    # Fill dummy variables for state
    if state == "Bangalore":
        data['State_Bangalore'] = 1
    elif state == "Chennai":
        data['State_Chennai'] = 1
    elif state == "Hyderabad":
        data['State_Hyderabad'] = 1
    # Base/Other state → all zeros

    # Convert to array in proper order
    input_array = np.array([data[col] for col in columns]).reshape(1, -1)
    st.write(input_array)

    # Predict
    prediction = model.predict(input_array)[0]

    st.success(f"Predicted Profit: ₹ {round(prediction, 2)}")