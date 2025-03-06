import streamlit as st

st.title("Medical diagnosis System")

pregnancies=st.number_input('Pregnancies',min value=0)
glucose=st.number_input('glucose level',min value=0)
bloood_pressure=st.number_input('Blood pressure',min value=0)
skin_thickness=st.number_input('skin thickness',min value=0)
insulin=st.number_input('insulin',min value=0)
bmi=st.number_input('BMI',min value=0)
diabetes_pedigree=st.number_input('Diabetes pedigree function',min_value=0.0)
age=st.number_input('Age',min_value=0)

if st.button('Predict')  
      input_data=np.array([Pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,Diabetes pedigree function.age]).reshape(1,-1)
      input_data=scaler.transform(input_data)
      prediction=model.predict(input_data)

      ifprediction==0;  
          st.write("Prediction: No Diabetes")
      else:
          st.write("Prediction: Diabetes")
          
