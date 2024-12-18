import streamlit as st

# App title
st.title("Simple Calculator App")

# Input fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation selection
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed!")
