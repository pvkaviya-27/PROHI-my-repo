import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng

page = st.sidebar.selectbox("Choose a page 👇", ["Dashboard", "About"])

if page == "Dashboard":
    st.write("# Welcome to the Season Prediction Dashboard!")
    st.image("https://wallpapercave.com/wp/wp4184896.jpg", width=800)

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

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# # Add a slider to the sidebar:
add_slider = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0)
 )
