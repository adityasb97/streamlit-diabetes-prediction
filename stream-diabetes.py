import pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# Membaca Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul Web
st.title("Aplikasi Prediksi Diabetes")
image = Image.open('diabetes.jpg')
st.image(image)

# membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies	= st.text_input("Input nilai Pregnancies")
with col2:
    Glucose = st.text_input("Input nilai Glucose")
with col1:
    BloodPressure = st.text_input("Input nilai Blood Pressure")
with col2:
    SkinThickness = st.text_input("Input nilai Skin Thickness")
with col1:
    Insulin = st.text_input("Input nilai Insulin")
with col2:
    BMI = st.text_input("Input nilai BMI")
with col1:
    DiabetesPedigreeFunction = st.text_input("Input nilai Diabetes Pedigree Function")
with col2:
    Age = st.text_input("Input nilai Age")

# Code Prediksi
diab_diagnosis = ''

# membuat tombol prediksi
if st.button("Test Prediksi diabetes"):
    X = pd.DataFrame({
    "Pregnancies": Pregnancies,
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    "SkinThickness": SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age

}, index=[0])
    diab_prediction = diabetes_model.predict(X)

    if(diab_prediction[0] == 1):
        diab_diagnosis = "Pasien TERKENA Diabetes"
        st.error(diab_diagnosis)
    else:
        diab_diagnosis = "Pasien TIDAK terkena Diabetes"

        st.success(diab_diagnosis)