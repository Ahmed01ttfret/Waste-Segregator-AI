import io
import tensorflow as tf
import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing import image as mg
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img





# Load logo image
logo = "Logo.jpg"

#container for the logo and title
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(logo, width=100)
    with col2:
        st.title("Waste Segregator AI")










st.write("""
        **Waste Segregator AI** This AI-powered waste classifier aims to simplify waste 
         segregation and enhance efficiency. Currently, performance is still in the early stages with moderate accuracy, 
         but this is only the beginning. Continuous improvements are underway, and contributions from users will help it 
         evolve over time.Feel free to upload waste images and be part of building a smarter, more sustainable future!

""")

def get_category(list):
    cat=['CLOTHES', 'ELECTRONIC','FOOD/ORGANIC','GLASS','METAL','PAPER','PLASTIC']
    index=list.index(1)
    return cat[index]

def load_model_(image_):
    model=load_model('my_modle.keras')
    


    

    # Make a prediction





    return get_category(model.predict(image_)[0].tolist())

    
    







st.write('Try Now')

# Upload image file
uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image using PIL for display purposes
    _image = Image.open(uploaded_file)

    # Display the image in the Streamlit app
    st.image(_image, caption="Uploaded Image", use_column_width=True)
    _image=_image.resize((150,150))
    image_arr=np.array(_image)
    imgage_arr = image_arr / 255.0

    # Add batch dimension (to make it shape (1, 150, 150, 3))
    img_tensor = tf.expand_dims(image_arr, axis=0)

    
    prediction = load_model_(img_tensor)
    
    # Display the prediction result
    st.write("Prediction: ", prediction)
    print(prediction)


    




# with st.sidebar:
#     st.title("Upload to help modle grow")
#     uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
#     option = st.selectbox("Choose an option:", ("CLOTH", "METAL", "PLASTIC", "FOOD", "ELECTRONIC", "GLASS", "PAPER"))
#     st.button("Submit")

    
    