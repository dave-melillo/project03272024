import streamlit as st

st.title("Simple Streamlit App")
    
# Add a slider widget for user input
number = st.slider("Select a number", 0, 100, 50)
    
# Compute the square of the number
square = number ** 2
    
# Display the result
st.write(f"The square of {number} is {square}")