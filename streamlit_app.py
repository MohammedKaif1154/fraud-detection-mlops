import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("💳 Fraud Detection System")

st.write("Enter transaction values:")

# Input box
input_data = st.text_area("Enter 30 values separated by comma")

if st.button("Predict"):
    try:
        data = list(map(float, input_data.split(",")))
        data = np.array(data).reshape(1, -1)

        prediction = model.predict(data)[0]

        if prediction == 1:
            st.error("🚨 Fraud Transaction Detected")
        else:
            st.success("✅ Normal Transaction")

    except:
        st.warning("⚠️ Please enter correct 30 values")