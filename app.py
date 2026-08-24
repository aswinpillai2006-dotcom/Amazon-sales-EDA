import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import os

# Set page config
st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐾", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction"])

# Load model function
@st.cache_resource
def load_model():
    model_path = 'cat_dog_classifier.keras'
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    return None

model = load_model()

if page == "Home":
    st.title("🐱🐶 Cat vs Dog Classifier")
    st.markdown("""
    ### Welcome to the Cat vs Dog Classification App!
    
    This application uses a Convolutional Neural Network (CNN) built with TensorFlow and Keras to classify images of cats and dogs.
    
    #### 📌 Navigation Guide:
    - **Home**: Overview of the application.
    - **Prediction**: Upload a single image and let the trained model predict whether it's a Cat or a Dog.
    
    👈 Use the sidebar on the left to navigate through the app.
    """)


elif page == "Prediction":
    st.title("🔮 Prediction")
    st.write("Upload an image to predict whether it is a Cat or a Dog.")
    
    if model is None:
        st.warning("⚠️ **Model not found!** Please ensure you have run the Jupyter Notebook to train and save the `cat_dog_classifier.keras` model in this directory.")
    else:
        uploaded_file = st.file_uploader("Upload an image...", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            # Display the uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image', width=300)
            
            if st.button("Predict"):
                with st.spinner("Predicting..."):
                    # Preprocess the image to match the model's input size (150x150)
                    img_resized = img.resize((150, 150))
                    img_array = image.img_to_array(img_resized)
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    # Make prediction
                    predictions = model.predict(img_array)
                    
                    # Assuming binary classification with 2 output nodes and softmax
                    # (Matching the notebook implementation)
                    score = tf.nn.softmax(predictions[0])
                    class_names = ['Cat', 'Dog']
                    
                    predicted_class = class_names[np.argmax(score)]
                    confidence = 100 * np.max(score)
                    
                    st.success(f"### This is a **{predicted_class}**!")
                    st.info(f"**Confidence:** {confidence:.2f}%")
