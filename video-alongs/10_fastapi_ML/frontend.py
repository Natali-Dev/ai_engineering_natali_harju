import streamlit as st
import httpx
from constants import ASSET_PATH

url = "http://127.0.0.1:8000/api/iris/predict"

def predict_flower(payload): 
    with httpx.Client(timeout=10) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        return response
    

st.markdown("# Predict iris flower")

with st.form("iris_data"):
    sep_len = st.number_input("Speal length(cm)", min_value = 4.01, max_value= 8.49, value=6.0, step=0.5)
        
    sep_wid = st.number_input("Sepal width (cm)", min_value=1.81, max_value=4.99, value=2.5, step=0.1)
        
    pet_len = st.number_input("Petal length (cm)", min_value=0.81, max_value=7.49, value=4.5, step=0.1)

    pet_wid = st.number_input("Petal width (cm)", min_value=0.01, max_value=2.99, value=1.2, step=0.1)

    submitted = st.form_submit_button("PREDICT")

if submitted:
    flower_info = {
        "sepal_length": float(sep_len),
        "sepal_width": float(sep_wid),
        "petal_length": float(pet_len),
        "petal_width": float(pet_wid)
        
        }
    st.markdown(flower_info)    
    response = predict_flower(payload=flower_info).json()
    flower = response.get("predicted_flower").casefold()
    st.markdown(response)
    st.markdown(f"Predicted flower based on your values: {flower}")
    
    st.image(f"{ASSET_PATH}/{flower}.jpg")
# st.number_input("Speal length(cm)", min_value = 4.01, max_value= 8.49)
# st.number_input("Speal length(cm)", min_value = 4.01, max_value= 8.49)
# st.number_input("Speal length(cm)", min_value = 4.01, max_value= 8.49)