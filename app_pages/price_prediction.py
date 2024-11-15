import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import plotly.express as px
import plotly.graph_objects as go
import os

def load_models():
    try:
        models = {
            'Linear Regression': joblib.load("models/linear_model.pkl"),
            'Random Forest': joblib.load("models/rf_model.pkl"),
            'Train Test Split': joblib.load("models/tts_model.pkl"),
            'ARD Regression': joblib.load("models/ard_model.pkl"),
            'KNN Regressor': joblib.load("models/knn_model.pkl")
        }
        return models
    except FileNotFoundError:
        st.error("Model files not found. Please check models directory.")
        return None
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None

def price_prediction_body():
    try:
        if not os.path.exists("models"):
            st.error("Models folder not found!")
            return

        required_models = ['linear_model.pkl', 'rf_model.pkl', 'tts_model.pkl', 
                         'ard_model.pkl', 'knn_model.pkl']
        missing_models = [model for model in required_models 
                         if not os.path.exists(f"models/{model}")]
        
        if missing_models:
            st.error(f"Missing model files: {', '.join(missing_models)}")
            return

        st.title("🏠 House Price Prediction")

        uploaded_file = st.file_uploader("Upload your file (CSV/Excel)", type=['csv', 'xlsx'])
        
        if uploaded_file is not None:
            try:
                
                if uploaded_file.size > 200 * 1024 * 1024:
                    st.error("File too large. Please upload a file smaller than 200MB")
                    return


                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                if df.empty:
                    st.error("The uploaded file is empty")
                    return
                    
                numeric_columns = ['sqft', 'bedrooms', 'bathrooms', 'floors', 'year_built']
                for col in numeric_columns:
                    if col in df.columns and not pd.to_numeric(df[col], errors='coerce').notnull().all():
                        st.error(f"Column {col} must contain only numeric values")
                        return

                st.write("Data Preview:")
                st.dataframe(df.head())
                
                required_columns = ['sqft', 'bedrooms', 'bathrooms', 'floors', 'year_built']
                if not all(col in df.columns for col in required_columns):
                    st.error("File harus memiliki kolom: sqft, bedrooms, bathrooms, floors, year_built")
                    return
                
                if st.button("Predict Prices"):
                    models = load_models()
                    if models is None:
                        return
                    
                    with st.spinner('Processing predictions...'):
                        predictions = {}
                        
                        for name, model in models.items():
                            predictions[name] = model.predict(df[required_columns])
                        
                        if 'actual_price' in df.columns:
                            scores = evaluate_predictions(df['actual_price'], predictions)
                            
                            st.write("Model Performance:")
                            performance_df = pd.DataFrame(scores).round(4)
                            st.dataframe(performance_df)
                            
                            best_model = max(scores.items(), key=lambda x: x[1]['R2'])[0]
                            st.success(f"Best performing model: {best_model}")
                            
                            df['predicted_price'] = predictions[best_model]
                            df['model_used'] = best_model
                        else:
                            for name, preds in predictions.items():
                                df[f'predicted_price_{name}'] = preds
                        
                        st.write("Prediction Results:")
                        st.dataframe(df)
                        
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Download Results",
                            data=csv,
                            file_name="price_predictions.csv",
                            mime="text/csv"
                        )
                
            except pd.errors.EmptyDataError:
                st.error("The uploaded file is empty")
            except pd.errors.ParserError:
                st.error("Error parsing the file. Please make sure it's a valid CSV/Excel file")
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e) 

if __name__ == "__main__":
    price_prediction_body()
