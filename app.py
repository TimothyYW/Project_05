import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary import summary_body

app = MultiPage(app_name="House prediction")  # Create an instance of the app

# Add your app pages here using .add_page()


app.run()  # Run the app