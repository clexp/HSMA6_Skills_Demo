import streamlit as st
import io
from PIL import Image
from rembg import remove

uploaded_image = st.file_uploader("Please upload an image file", type=['png','jpg','jpeg','bmp', 'bitmap'])

if uploaded_image is not None:

    imagefile = io.BytesIO(uploaded_image.read())

    im = Image.open(imagefile)

    img_edited = remove(im)

    st.write("Original Image")
    st.image(uploaded_image)

    st.write("Edited Image")
    st.image(img_edited)
