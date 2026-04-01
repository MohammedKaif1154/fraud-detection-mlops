import streamlit as st
import pickle
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("💳 Fraud Detection System")

st.write("Enter transaction values:")

# Input box
input_data = st.text_area("Enter 30 values separated by comma")

if st.button("🔍 Predict"):
    try:
        data = list(map(float, input_data.split(",")))
        
        if len(data) != 30:
            st.warning("⚠️ Please enter exactly 30 values")
        else:
            data = np.array(data).reshape(1, -1)
            
            prediction = model.predict(data)[0]
            prob = model.predict_proba(data)[0][1]

            if prediction == 1:
                st.error("🚨 Fraud Transaction Detected")
            else:
                st.success("✅ Normal Transaction")

            # 👉 Show probability
            st.write(f"💡 Fraud Probability: {prob:.2f}")

    except:
        st.error("❌ Invalid input format")