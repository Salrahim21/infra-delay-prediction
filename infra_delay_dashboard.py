import streamlit as st
import pandas as pd
import pickle

# Load model
with open("delay_model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("🏗️ Infrastructure Delay Estimator")

# Collect user inputs
height = st.number_input("Height (m)", min_value=1.0, max_value=1000.0)
floors = st.number_input("Number of Floors", min_value=1, max_value=300)

material_used = st.selectbox("Material Used", ['Steel', 'Concrete', 'Other'])
function = st.selectbox("Function", ['Residential', 'Office', 'Mixed-use', 'Other'])
country = st.selectbox("Country", ['USA', 'China', 'UAE', 'India', 'Other'])

# Encode categorical inputs — same logic as model training
material_map = {'Steel': 2, 'Concrete': 1, 'Other': 0}
function_map = {'Residential': 0, 'Office': 1, 'Mixed-use': 2, 'Other': 3}
country_map = {'USA': 0, 'China': 1, 'UAE': 2, 'India': 3, 'Other': 4}

material_encoded = material_map[material_used]
function_encoded = function_map[function]
country_encoded = country_map[country]

# Create input DataFrame in exact order used during training
X_input = pd.DataFrame([[height, floors, material_encoded, function_encoded, country_encoded]],
                       columns=['height_(m)', 'floors', 'material_used', 'function', 'country'])

# Predict
if st.button("Estimate Duration"):
    prediction = model.predict(X_input)[0]
    st.success(f"⏱️ Estimated Construction Duration: {prediction:.2f} months")
