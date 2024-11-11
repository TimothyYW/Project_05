# price_prediction.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


def load_model():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model


def predict_price(model, input_data):
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(input_data)
    
    
    predicted_price = model.predict(scaled_data)
    return predicted_price[0]


def show_predict_page():
    st.title("House Price prediction")

    
    st.sidebar.header('Masukkan Fitur Rumah')
    sqft = st.sidebar.number_input("Luas Rumah (dalam m²)", min_value=0, value=150)
    bedrooms = st.sidebar.number_input("Jumlah Kamar Tidur", min_value=1, value=3)
    bathrooms = st.sidebar.number_input("Jumlah Kamar Mandi", min_value=1, value=2)
    floors = st.sidebar.number_input("Jumlah Lantai", min_value=1, value=1)
    year_built = st.sidebar.number_input("Tahun Dibangun", min_value=1900, value=2000)
    
    
    input_data = np.array([[sqft, bedrooms, bathrooms, floors, year_built]])

    
    if st.sidebar.button("Prediksi Harga"):
        model = load_model()
        predicted_price = predict_price(model, input_data)

       
        st.subheader(f"Price Predicted: ${predicted_price:,.2f}")
        st.write("The Price of the house is:")


if __name__ == "__main__":
    show_predict_page()
