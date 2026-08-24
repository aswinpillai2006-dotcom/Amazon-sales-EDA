import streamlit as st
import numpy as np
import joblib
import os

st.set_page_config(page_title="Heart Disease Predictor")

# Check if model files exist
if not os.path.exists('heart_model.pkl') or not os.path.exists('scaler.pkl'):
    st.error("Error: Run 'python mls.py' first to create model files")
    st.stop()

model = joblib.load('heart_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("❤️ Heart Disease Risk Predictor")

col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 20, 80, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type 0-3", [0,1,2,3])
    trestbps = st.number_input("Resting BP", 90, 200, 130)
    chol = st.number_input("Cholesterol", 120, 600, 250)
    fbs = st.selectbox("Fasting BS > 120", [0,1])

with col2:
    restecg = st.selectbox("Rest ECG 0-2", [0,1,2])
    thalach = st.number_input("Max Heart Rate", 70, 220, 150)
    exang = st.selectbox("Exercise Angina", [0,1])
    oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0, step=0.1)
    slope = st.selectbox("Slope 0-2", [0,1,2])
    ca = st.selectbox("Major Vessels 0-3", [0,1,2,3])
    thal = st.selectbox("Thal 0-3", [0,1,2,3])

if st.button("Predict"):
    sex_val = 1 if sex == "Male" else 0
    data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)[0]
    prob = model.predict_proba(data_scaled)[0][1]

    if pred == 1:
        st.error(f"⚠️ High Risk: {prob*100:.1f}%")
    else:
        st.success(f"✅ Low Risk: {(1-prob)*100:.1f}%")