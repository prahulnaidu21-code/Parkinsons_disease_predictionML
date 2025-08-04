import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Parkinson's Predictor", page_icon="🧠", layout="centered")

st.title("🧠 Parkinson's Disease Detection App")
st.markdown("Enter the following **voice measurements** to predict Parkinson’s disease.")

feature_names = [
    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)',
    'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ',
    'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
    'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
    'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
]

inputs = []
col1, col2 = st.columns(2)
for idx, feature in enumerate(feature_names):
    with (col1 if idx % 2 == 0 else col2):
        val = st.number_input(f"{feature}", value=0.0, step=0.000001, format="%.6f")
        inputs.append(val)

if st.button("🔍 Predict"):
    if all(i == 0.0 for i in inputs):
        st.warning("Please enter values for prediction.")
    else:
        input_array = np.array(inputs).reshape(1, -1)
       
        prediction = model.predict(input_array)[0]  # Ensure this line is present and correct

        if prediction == 1:
            st.error("🔴 Parkinson's Detected")
        else:
            st.success("🟢 No Parkinson's Detected")

