import streamlit as st
import numpy as np

# Title and description
st.set_page_config(page_title="California House Price Predictor")
st.title("🏠 California House Price Predictor")
st.markdown("""
This app uses a custom-trained **Linear Regression** model to predict the **median house price** in California based on various features.  
Model trained on the official **California Housing Dataset**.
""")

# Feature inputs
st.subheader("Enter the following features:")
MedInc = st.number_input("Median Income (10k USD)", value=5.0, min_value=0.0)
HouseAge = st.number_input("House Age (years)", value=20.0, min_value=0.0)
AveRooms = st.number_input("Average Number of Rooms", value=5.0, min_value=0.0)
AveBedrms = st.number_input("Average Number of Bedrooms", value=1.0, min_value=0.0)
Population = st.number_input("Block Population", value=1000.0, min_value=0.0)
AveOccup = st.number_input("Average Occupants per Household", value=3.0, min_value=0.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

# Normalize the inputs using the same mean and std used during training
X_input = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])

# Training set stats (mean and std) from the original dataset
mean = np.array([3.870671, 28.639486, 5.429, 1.096, 1425.0, 3.07, 35.63, -119.57])
std = np.array([1.9, 12.59, 2.45, 0.47, 1132.5, 1.0, 2.13, 2.0])

X_norm = (X_input - mean) / std

# Model weights and bias from your training
weights = np.array([ 0.81661663,  0.17689642, -0.12729395,  0.14126483,  
                     0.01664059, -0.04392217, -0.48604356, -0.44966799])
bias = 2.0684688668526414

# Prediction
prediction = float(np.dot(X_norm, weights) + bias)

# Display result
st.subheader("📈 Predicted Median House Value")
st.success(f"${prediction:.2f} (in 100,000s USD)")
st.caption("For example, $2.35 means ~$235,000")

# Footer
st.markdown("---")
