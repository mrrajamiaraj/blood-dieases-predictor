import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load('blood_disease_model.pkl')
    le = joblib.load('diagnosis_label_encoder.pkl')
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

st.title("🩺 Blood Disease Predictor")
st.write("Enter your blood test values to predict the diagnosis:")

HGB = st.number_input("Hemoglobin (HGB)", 5.0, 20.0, 13.5)
HCT = st.number_input("Hematocrit (HCT)", 20.0, 60.0, 40.0)
MCV = st.number_input("Mean Corpuscular Volume (MCV)", 60.0, 110.0, 85.0)
MCH = st.number_input("MCH", 20.0, 35.0, 28.0)
MCHC = st.number_input("MCHC", 20.0, 40.0, 33.0)
RBC = st.number_input("Red Blood Cells (RBC)", 3.0, 6.5, 4.5)
WBC = st.number_input("White Blood Cells (WBC)", 3000, 12000, 7000)
PLT = st.number_input("Platelet Count (PLT)", 100000, 500000, 250000)
LYMn = st.number_input("Lymphocyte Count (LYMn)", 0.5, 5.0, 2.0)
LYMp = st.number_input("Lymphocyte % (LYMp)", 10, 60, 30)
NEUTn = st.number_input("Neutrophil Count (NEUTn)", 1.0, 8.0, 4.0)
NEUTp = st.number_input("Neutrophil % (NEUTp)", 30, 80, 55)
PCT = st.number_input("Plateletcrit (PCT)", 0.1, 1.0, 0.3)
PDW = st.number_input("Platelet Distribution Width (PDW)", 10.0, 20.0, 14.0)

if st.button("Predict Diagnosis"):
    input_data = pd.DataFrame([[
        HGB, HCT, MCV, MCH, MCHC, RBC, WBC, PLT,
        LYMn, LYMp, NEUTn, NEUTp, PCT, PDW
    ]], columns=[
        'WBC', 'LYMp', 'NEUTp', 'LYMn', 'NEUTn', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'PLT', 'PDW', 'PCT'
    ])

    prediction = model.predict(input_data)
    diagnosis = le.inverse_transform(prediction)[0]

    st.success(f"🧬 Predicted Diagnosis: **{diagnosis}**")

