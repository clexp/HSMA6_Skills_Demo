import streamlit as st

uploaded_image = st.file_uploader("Please upload an image file", type=['png','jpg','jpeg','bmp', 'bitmap'])

if uploaded_image is not None:

    st.write("Here's the image you have uploaded")

    st.image(uploaded_image)

else:

    st.write("You haven't uploaded anything yet!")
