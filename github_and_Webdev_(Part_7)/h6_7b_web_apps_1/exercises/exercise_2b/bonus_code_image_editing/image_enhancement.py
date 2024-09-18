import streamlit as st
import io
from PIL import Image, ImageEnhance
import PIL.ImageOps

uploaded_image = st.file_uploader("Please upload an image file", type=['png','jpg','jpeg','bmp', 'bitmap'])

if uploaded_image is not None:

    imagefile = io.BytesIO(uploaded_image.read())

    im = Image.open(imagefile)

    threshold = st.slider("Choose a threshold", 1, 100, value=80, step=1)
    contrast_factor = st.slider("Contrast Enhancement Strength", 0.0, 2.0, value=1.0, step=0.05)
    invert = st.checkbox("Invert Output Image?")

    enhancer = ImageEnhance.Contrast(im)
    img_edited = enhancer.enhance(contrast_factor)

    img_edited = img_edited.convert("L").point(
        lambda x: 255 if x > threshold else 0
    )

    if invert:
        img_edited = PIL.ImageOps.invert(img_edited)

    st.write("Original Image")
    st.image(uploaded_image)

    st.write("Edited Image")
    st.image(img_edited)
