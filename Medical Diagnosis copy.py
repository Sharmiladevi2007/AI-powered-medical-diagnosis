import streamlit as st
import numpy as np
from sklearn.preprocessing import Standardscaler
from sklearn.ensemble import Random ForestClassifier
import pickle

model=pickle.load(open('trained_model,pkl','rb'))
scaler=pickle.looad(open('scaler.pkl','rb))

def recognize_face():
    pass

def predict_medical_condition(data):
    data_scaled = scaler.transform([data])
    prediction = model.predict(data_scaled)
    return prediction

st.title("Medical Diagnosis System with Face Recognition")

recognize_face()

pregnancies = st.number_input('Pregnancies',min value=0)
glucose=st.number_input('Glucose',min value=0)
blood_pressure=st.nmbre_input('Blood_pressure',min value=0)
skin_thickness=st.number_input('Skin_thickness'min value=0)
insulin=st.number_input('insulin',min value=0)
bmi=st.number_input('BMI',min value=0.0)
diabetes_pedigree=st.number_input('Diabetes pedigree Function',min_value=0)
age=st.number_input('Age',min value=0)

data=[Pregnancies,Glucose,Blood_Pressure,Skin_thickness,insulin,bmi,diabetes_pedigree,age]

if st.button('Predict'):
    diagnosis=predict_medical_condition(data)
    if diagnosis==0:
        st.write("Pediction: No Diabetes")
    else:
        st.wtite("Prediction: Diabetes")


                  
            

