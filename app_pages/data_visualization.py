import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# from matplotlib.image import imread



def sale_price_correlation():
    

    st.write("Corralations with sale price")

    correlation_analysis = plt.imread(
        "outputs/correlation_analysis.png")
    st.image(correlation_analysis,
            caption='Correlation with sale price')
    st.write("---")

    st.write("### Model History")
    
    model_residual = plt.imread(f"outputs/residual_plot.png")
    st.image(model_residual, caption='Error in prediction in sale price')
    
    st.write("---")

    st.write("### Time of prediction for large and small data set")
    st.dataframe(pd.DataFrame("outputs/time_prediction.csv"))
                 
    st.write("---")