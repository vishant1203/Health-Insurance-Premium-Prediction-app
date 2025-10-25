import streamlit as st
import numpy as np
from prediction_helper import predict

# --- Page Config ---
st.set_page_config(page_title="Vishant", page_icon="💰", layout="wide")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>💰 Health Insurance Premium Prediction</h1>", unsafe_allow_html=True)
st.write("### Fill in the details below to estimate your insurance premium:")

# --- Layout ---
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", min_value=0, max_value=120, value=30)
        Gender = st.selectbox("Gender", ['Male', 'Female'])
        Region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
        Marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
        BMI_Category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
        Smoking_Status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])

    with col2:
        Employment_Status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer', 'NA'])
        Income_Level = st.selectbox("Income Level", ['<10L', '10L - 25L', '25L - 40L', '> 40L', 'NA'])
        Medical_History = st.selectbox("Medical History", [
            'No Disease', 'Diabetes', 'High blood pressure',
            'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
            'High blood pressure & Heart disease', 'Diabetes & Thyroid', 'Diabetes & Heart disease'
        ])
        Insurance_Plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
        Number_Of_Dependants = st.number_input("Number of Dependants", min_value=0, value=0)
        Income_Lakhs = st.number_input("Annual Income (Lakhs)", min_value=0.0, value=5.0)
        Genetical_Risk = st.slider("Genetical Risk (%)", min_value=0, max_value=100, value=1)

# --- Input Dictionary ---
input_data = {
    'Gender': Gender,
    'Region': Region,
    'Marital_status': Marital_status,
    'BMI_Category': BMI_Category,
    'Smoking_Status': Smoking_Status,
    'Employment_Status': Employment_Status,
    'Income_Level': Income_Level,
    'Medical_History': Medical_History,
    'Insurance_Plan': Insurance_Plan,
    'Age': Age,
    'Number_Of_Dependants': Number_Of_Dependants,
    'Income_Lakhs': Income_Lakhs,
    'Genetical_Risk': Genetical_Risk
}

# --- Prediction Button ---
st.markdown("<br>", unsafe_allow_html=True)  # spacing
if st.button("🔍 Calculate Premium", use_container_width=True):
    prediction = predict(input_data)
    st.success(f"✅ Predicted Health Insurance Cost: **₹ {prediction}**")

