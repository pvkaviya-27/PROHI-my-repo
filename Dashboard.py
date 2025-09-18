import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng

page = st.sidebar.selectbox("Choose a page 👇", ["Dashboard", "About"])

if page == "Dashboard":
    st.write("# Welcome to the Season Prediction Dashboard!")
    #st.image("https://wallpapercave.com/wp/wp4184896.jpg", width=800)
    st.image("assets/image.jpg", width=800)

    df = np.random.randn(100)
    df = pd.DataFrame({"Temperature (°C)": rng(0).integers(-25, 40, size=100),
                       "Precipitation (mm)": rng(0).integers(0, 110, size=100),
                       "UV Index": rng(0).integers(0, 14, size=100)
                       })
    
    st.subheader("Synthetic Data:")
    st.dataframe(df)
    
    st.header("Enter Input Features:")
    temp = st.slider("Temperature (°C)", min_value=-25, max_value=40, value=25)
    prec = st.slider("Precipitation (mm)", min_value=0, max_value=110, value=40)
    uv = st.slider("UV Index", min_value=0, max_value=14, value=3)

    st.button(label="Predict", icon="⁉️")

    st.subheader("Data Chart:")
    st.line_chart(df)

elif page == "About":
    st.title("Kaviya Palaniyappan")
    st.subheader("Summary of the project:")

    st.markdown("""
                This interactive dashboard was developed to predict the seasons using inputs of **Temperature**, **Precipitation**, and **UV index**.
                By analyzing these parameters, the model classifies conditions into spring, summer, autumn, or winter.
                
                This model was developed using simple machine learning algorithms, such as random forest classifier, trained on a synthetic dataset to map input values to seasonal outcomes.
                An example prediction includes,
                  - elevated temperatures above 25°C combined with high UV index (above 8) typically indicate summer,
                  - while temperatures below 5°C and precipitation over 50mm suggest winter.
                
                Users can interact via sliders to adjust variables, and obtain a prediction.
                Future iterations could integrate real API data for live forecasting, enhancing accuracy and usability in educational or practical settings.

""")
# # Page information
