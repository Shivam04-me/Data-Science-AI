

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

data = pd.read_csv("multiple_linear_salary_dataset_50_records.csv")
X = data[["Experience", "Education_Level", "Age"]]
y = data["Salary"]
model = LinearRegression()
model.fit(X, y)
st.title("Employee Salary Prediction")

experience = st.sidebar.slider(
    "Years of Experience",
    min_value=int(data["Experience"].min()),
    max_value=int(data["Experience"].max()),
    value=int(data["Experience"].min())
)

education = st.sidebar.slider(
    "Education Level (Years)",
    min_value=int(data["Education_Level"].min()),
    max_value=int(data["Education_Level"].max()),
    value=int(data["Education_Level"].min())
)

age = st.sidebar.slider(
    "Age",
    min_value=int(data["Age"].min()),
    max_value=int(data["Age"].max()),
    value=int(data["Age"].min())
)

if st.button("Predict Salary"):
    prediction = model.predict([[experience, education, age]])

    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")