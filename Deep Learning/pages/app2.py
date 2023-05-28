import os
import streamlit as st
import plotly.express as px
from helpers import predictor

def app():
    st.write("# Plant Leaf Disease Classification")

    st.write("## Upload Image in .jpg format")
    uploaded_image = st.file_uploader("", type=["jpg"])

    st.write("## Uploaded Image")

    if uploaded_image:
        st.image(uploaded_image)

        button = st.button("Classify", key=None)

        if button:
            prediction, predicted_class = predictor.predict(uploaded_image)

            labels = {0:'Apple___Apple_scab',1:'Apple___Black_rot',2:'Apple___Cedar_apple_rust',3:'Apple___healthy',
               4:'Blueberry___healthy',5:'Cherry_(including_sour)___healthy',6:'Cherry_(including_sour)___Powdery_mildew',
               7:'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',8:'Corn_(maize)___Common_rust_',9:'Corn_(maize)___healthy',
               10:'Corn_(maize)___Northern_Leaf_Blight',11:'Grape___Black_rot',12:'Grape___Esca_(Black_Measles)',
               13:'Grape___healthy',14:'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',15:'Orange___Haunglongbing_(Citrus_greening)',
               16:'Peach___Bacterial_spot',17:'Peach___healthy',18:'Pepper,_bell___Bacterial_spot',19:'Pepper,_bell___healthy',
               20:'Potato___Early_blight',21:'Potato___healthy',22:'Potato___Late_blight',23:'Raspberry___healthy',
               24:'Soybean___healthy',25:'Squash___Powdery_mildew',26:'Strawberry___healthy',27:'Strawberry___Leaf_scorch',
               28:'Tomato___Bacterial_spot',29:'Tomato___Early_blight',30:'Tomato___healthy',31:'Tomato___Late_blight',
               32:'Tomato___Leaf_Mold',33:'Tomato___Septoria_leaf_spot',34:'Tomato___Spider_mites Two-spotted_spider_mite',
               35:'Tomato___Target_Spot',36:'Tomato___Tomato_mosaic_virus',37:'Tomato___Tomato_Yellow_Leaf_Curl_Virus'}

            classes=[]
            prob=[]
            for i,j in enumerate (prediction[0], 0):
                classes.append(labels[i].capitalize())
                prob.append(round(j*100,2))

            fig = px.bar(x=classes, y=prob,
                         text=prob, color=classes,
                         labels={"x":"Disease", "y":"Probability(%)"})

            st.markdown("#### Probability Distribution Bar Chart", True)
            st.plotly_chart(fig)

            st.markdown(f"#### The Image Is Classified As`{predicted_class.capitalize()}` With A Probability Of `{max(prob)}%`", True)
            
    else:
        st.write("#### No Image Was Found, Please Retry!!!")