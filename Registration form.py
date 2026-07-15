import streamlit as st
st.set_page_config(page_title="Student Registration form",page_icon="")
st.title("Student Registration form ")
name = st.text_input("Student name ")
father = st.text_input("Father's name ")
email = st.text_input("Email")
contact = st.text_input("Enter contact ")
gender = st.radio("Gender",["Female", "Male"])
age= st.number_input("Age", min_value=18, max_value=50, step =1)
course = st.selectbox("Course",["B.Tech", "BCA", "B.Com", "B.Sc", "M.Tech", "MBA"])
branch = st.selectbox("Branch",["Computer Science", "Data Science ", "AI & ML", "Information Technology", "Electronics", "Mechanical"])
semester =st.selectbox("Semester",[1,2,3,4,5,6,7,8])
add= st.text_area("Address")
agree = st.checkbox("I agree that the above information is correct ")
if st.button("Register"):
    if name =="" or email =="" or contact == "":
        st.error("Please fill all the required fields ")
    elif not agree:
        st.warning("Please accept the declaration")
    else:
        st.success("Student Registration Successfully !")
        st.subheader("Registration Details ")
        
        st.write("**Name**", name)
        st.write("**father**",father)
        st.write("**Email**", email)
        st.write("**contact**", contact)
        st.write("**Gender**", gender)
        st.write("**Course:**", course)
        st.write("**Branch:**", branch)
        st.write("**Semester:**", semester)
        st.write("**Address:**", add)