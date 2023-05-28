import streamlit as st
import os

def app():
    st.title("Plant Leaf Disease Classification")

    st.subheader("Objective :")
    st.markdown("The main Objective of this project is to use `Deep learning` to classify plant leaf disease images into 38 different classes namely :", True)
    
    st.subheader("Motivation :")
    st.markdown("This Project has been created as part of the <b>Final Year Project</b> presented by: Harsh Vardhan, Vikram Kumar and Rishi Raj, students of  <b>Bengal Institute Of Technology</b>", True)

    st.markdown("<hr/>", True)

    st.subheader("Description :")
    st.markdown("This Project uses `Fine Tuned EfficientNetB3 Model` which is a Pre-Trained CNN Model from Keras/Tensorflow.", True)
    st.markdown("It Gave the `Highest Accuracy of 99.5%` while classifying image from test set.", True)

    st.markdown("<hr/>", True)


    