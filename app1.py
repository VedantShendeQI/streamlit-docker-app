import streamlit as st

# Page Title
st.title("🚀 My Smart Docker App")

# Sidebar Menu
option = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Calculator", "Temperature Converter"]
)

# ---------------- HOME ----------------
if option == "Home":
    st.header("Welcome 👋")
    name = st.text_input("Enter your name")

    if name:
        st.success(f"Hello {name}, welcome to your Docker app!")

# ---------------- CALCULATOR ----------------
elif option == "Calculator":
    st.header("🧮 Simple Calculator")

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    operation = st.selectbox("Choose operation", [
                             "Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
                result = None

        if result is not None:
            st.success(f"Result: {result}")

# ---------------- TEMPERATURE ----------------
elif option == "Temperature Converter":
    st.header("🌡 Temperature Converter")

    temp = st.number_input("Enter temperature", value=0.0)
    unit = st.selectbox(
        "Convert to",
        ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    )

    if st.button("Convert"):
        if unit == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            st.success(f"{temp}°C = {result}°F")
        else:
            result = (temp - 32) * 5/9
            st.success(f"{temp}°F = {result}°C")
