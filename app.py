import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary import summary_body
from app_pages.hypothesis import project_hypothesis_body

app = MultiPage(app_name="House prediction")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page('Project Summary', summary_body)
app.add_page('Project Hypothesis and Validation',project_hypothesis_body)

app.run()  # Run the app