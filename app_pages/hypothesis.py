import streamlit as st

def project_hypothesis_body():

    st.write('### Project Hypothesis and Validation')

    st.success(
        'The correlation with SalePrice has interesting results:'
        '\n* 1. OverallQual, YearBuilt, and YearRemodADD are the highest positive correlation with SalePrice'
        '\n* 2. Categories BsmtExposure_No, GarageFinish_Unf, and KitchenQual_TA are the highest negative correlation with SalePrice'
        '\n* 3. 1stFlrSF and EnclosedPorch has the lowest correlation with SalePrice'
        'So times and the quality has an effect to the sale of houses'
    )

    st.warning(
        'Through the feature important the result correlation will be tested, and the result is stated something different:'
        '\n* 1. Overall quality dominatly important'
        '\n* 2. 2ndFlrSF, GrLivArea are the second and third most important feature'
        '\n* 3. BsmtFinType1_BLQ, BsmtFinType1_LWQ, and EnclosedPrch are three least important features'
    )