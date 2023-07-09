
import streamlit as st
import base64
import datetime
import time

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
      """
st.markdown(hide_default_format, unsafe_allow_html=True)


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.png")
page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://plus.unsplash.com/premium_photo-1682417576991-490b1185cbc2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1957&q=80");
background-size:20%;
background-position: top ;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('  AI Job Consultancy (Pune)')
st.selectbox(' Choose your job requirement',['Data Analyst','Machine Learning Engineer','Data Scientist'])
st.text_input('Name')
st.text_input('Email address')
st.selectbox(' Choose your shift time',['shift-1(9am-5pm)','shift-2(6pm-3am)'])
st.text_area('Brief about past projects and job experiences')
st.file_uploader('Upload your resume')
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose your qualification',['Masters', 'Graduate', 'Undergraduate'])
st.multiselect('Python Proficiency lebel',['Beginner', 'Intermediate', 'Advanced'])
st.multiselect('Machine Learning Proficiency lebel',['Beginner', 'Intermediate', 'Advanced'])
st.number_input('Selecxt your relevant experience',0,3)
st.slider('justify how eligible you are for this job', 0,10)
