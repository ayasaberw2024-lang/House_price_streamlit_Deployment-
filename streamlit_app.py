#1- import the required lib 
import streamlit as st
import pandas as pd
import joblib

#2- load the model , scaler , columns what ever u need to the prediction 

model = joblib.load("XG_model.joblib")
columns = joblib.load("columns.pkl")

#3- empty place to put the  user input in 
input_data = {}


#4- loop  to just put the number input but 
for col in columns:
    #check if it's the categorical feature  map it with ur hands 
    if col == "CentralAir":
        val = st.selectbox(col, ["Y", "N"])
        input_data[col] = 1 if val == "Y" else 0
    else:
        input_data[col] = st.number_input(col, value=0.0)

#if the user press the button 
if st.button("Predict"):
    input_df = pd.DataFrame([input_data])

    # مهم جدًا: نفس ترتيب التدريب
    input_df = input_df[columns]

    prediction = model.predict(input_df)

    st.success(f"🏠 Predicted Price: ${prediction[0]:,.2f}")