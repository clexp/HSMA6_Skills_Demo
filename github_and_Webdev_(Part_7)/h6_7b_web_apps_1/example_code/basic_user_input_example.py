import streamlit as st

st.title('Simple Calculator App')

num_1 = st.number_input(label="First Number", step=1, value=10)

num_2 = st.number_input(label="Second Number", step=1, value=10)

operator = st.radio(label="Operation",
                    options=["Add", "Subtract", "Multiply", "Divide"])

if operator == "Add":
    output = num_1 + num_2
elif operator == "Subtract":
    output = num_1 - num_2
elif operator == "Multiply":
    output = num_1 * num_2
elif operator == "Divide":
    output = num_1 / num_2

st.text(f"The answer is {output}")
