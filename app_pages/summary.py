import streamlit as st

def summary_body():

    st.write('### Project Summary')

    st.info(
        'House prediction is a project for predict analytic machine learning'
        'This project helps clients to analyse what is the important features that are affecting the house pricing'
        'And also give them a modal that can be use to predict the pricing'
        )

    st.success(
        'The project has 2 business requirements:'
        '\n* 1. - The client is interested in discovering how the house attributes correlate with the sale price.'
        '\n* 2. - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.'
        )