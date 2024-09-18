import streamlit as st

st.write("Look at this penguin!")

filename = "penguin.jpg"

st.image(filename)

with open(filename, "rb") as img:
    btn = st.download_button(
        label="Download image",
        data=img,
        file_name=filename,
        mime="image/png"
    )
