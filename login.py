import streamlit as st
import pandas as pd
import time

# Sidebar
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Select Page", ["Login"])

st.title("User Login Form")
st.header("Login Details")
st.subheader("Enter Your Information")
st.caption("Demo Login Form")

# Input Widgets
uid = st.text_input("User ID")
pswd = st.text_input("Password", type="password")
age = st.number_input("Age", 18, 100)
gender = st.radio("Gender", ["Male", "Female"])
course = st.selectbox("Course", ["Python", "AI", "ML", "Data Science"])
skills = st.multiselect("Skills", ["Python", "Java", "SQL", "C++"])
agree = st.checkbox("I Agree to Terms & Conditions")
dob = st.date_input("Date of Birth")
tm = st.time_input("Login Time")
color = st.color_picker("Favorite Color")

uploaded_file = st.file_uploader("Upload Profile Photo")

st.divider()

# Columns
col1, col2 = st.columns(2)

with col1:
    login = st.button("Login")

with col2:
    reset = st.button("Reset")

# Login Button
if login:
    if uid == "" or pswd == "":
        st.warning("Fill all fields")
    elif uid == "admin" and pswd == "1234":
        with st.spinner("Checking..."):
            time.sleep(2)

        progress = st.progress(0)
        for i in range(101):
            progress.progress(i)
            time.sleep(0.01)

        st.success("Login Successful")
        st.balloons()

        st.metric("Login Count", 1)

        data = pd.DataFrame({
            "User": [uid],
            "Course": [course],
            "Age": [age]
        })

        st.dataframe(data)
        st.table(data)

        st.json({
            "User": uid,
            "Gender": gender,
            "Skills": skills
        })

    else:
        st.error("Invalid User ID or Password")

# Reset Button
if reset:
    st.info("Reset Button Clicked")

# Expander
with st.expander("Show Instructions"):
    st.write("User ID : admin")
    st.write("Password : 1234")

st.markdown("**Thank You for Using Streamlit**")
st.code("print('Login Successful')")
st.latex(r"y=mx+c")