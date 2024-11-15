import streamlit as st
from app_pages.price_prediction import price_prediction_body
from app_pages.summary import summary_body

def main():
    st.set_page_config(
        page_title="House Price Prediction",
        page_icon="🏠",
        layout="wide"
    )

    pages = {
        "Summary": summary_body,
        "Price Prediction": price_prediction_body
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()