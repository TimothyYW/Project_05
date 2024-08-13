import streamlit as st

def page_summary_body():

    st.write('### Quick Project Summary')

    st.info(
        'Brain Tumor Detector is a data science and machine learning project. '
        'The business goal of this project is the differentiation of the '
        'healthy brain and the one with the tumor based on the brain MRI '
        'scan images. The project is realised with the Streamlit Dashboard '
        'and gives to the client a possibility to upload the MRI brain scan '
        'in order to predict the possible tumor diagnosis. The dashboard '
        'offers the results of the data analysis, description and the '
        'analysis of the project\'s hypothesis, and details about the '
        'performance of the machine learning model.'
        )

    st.success(
        'The project has 2 business requirements:\n'
        '1. The client is interested in discovering how the house attributes correlate with the sale price.'
        '2. The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.'
        )