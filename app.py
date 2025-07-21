import streamlit as st
import pandas as pd
import numpy as np
import joblib  # 🔥 THIS IS THE LINE THAT FAILS IF joblib IS MISSING

# Load trained model and columns
model = joblib.load("salary_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("💼 Employee Salary Predictor")

# Input form
st.subheader("Enter Employee Details")
age = st.number_input("Age", min_value=18, max_value=70, value=30)
experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=3)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"])

# Create input DataFrame
input_data = {
    'Age': age,
    'Years of Experience': experience,
    'Gender_Male': 1 if gender == 'Male' else 0,
    "Education Level_Master's": 1 if education == "Master's" else 0,
    "Education Level_PhD": 1 if education == "PhD" else 0,
    'Job Title_Data Analyst': 1 if job == 'Data Analyst' else 0,
    'Job Title_Director': 1 if job == 'Director' else 0,
    'Job Title_Sales Associate': 1 if job == 'Sales Associate' else 0,
    'Job Title_Senior Manager': 1 if job == 'Senior Manager' else 0,
    'Job Title_Software Engineer': 1 if job == 'Software Engineer' else 0
}

# Ensure correct column order
input_df = pd.DataFrame([input_data], columns=columns)

# Predict
if st.button("Predict Salary"):
    salary = model.predict(input_df)[0]
    st.success(f"💰 Estimated Salary: ₹{int(salary):,}")
