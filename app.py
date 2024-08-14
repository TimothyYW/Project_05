import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary import summary_body
from app_pages.hypothesis import project_hypothesis_body
from app_pages.price_prediction import price_prediction_body
from app_pages.data_visualization import data_visualization_body

app = MultiPage(app_name="House prediction")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page('Project Summary', summary_body)
app.add_page('Data Visualization',data_visualization_body)
app.add_page('Price Prediction', price_prediction_body)
app.add_page('Project Hypothesis and Validation',project_hypothesis_body)


app.run()  # Run the app