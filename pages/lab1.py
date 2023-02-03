import streamlit as st
# import cv2

st.title("lab1")

# file = st.file_uploader("upload_file")

file = st.file_uploader("input_file")

if file is None:
    file = st.camera_input("take picture")


st.download_button("사진을 다운로드 하셈", file)

