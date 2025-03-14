import streamlit as st

# Page configuration
st.set_page_config(page_title="Simple Calculator", page_icon="🔢", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📱 Simple Calculator</h1>", unsafe_allow_html=True)
st.write("### 🔢 Enter two numbers and choose an operation:")

# Two columns for number input
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.radio("Choose operation:", ["➕ Addition", "➖ Subtraction", "✖ Multiplication", "➗ Division"])

# Calculate button
if st.button("💡 Calculate"):
    try:
        if operation == "➕ Addition":
            result = num1 + num2
            symbol = "+"
        elif operation == "➖ Subtraction":
            result = num1 - num2
            symbol = "-"
        elif operation == "✖ Multiplication":
            result = num1 * num2
            symbol = "×"
        else:  # ➗ Division
            if num2 == 0:
                st.error("❌ Error: Division by zero!")
                st.stop()
            result = num1 / num2
            symbol = "÷"

        # Styled result display
        st.success(f"✅ **Result:** {num1} {symbol} {num2} = **{result}**")

    except Exception as e:
        st.error(f"⚠ An error occurred: {str(e)}")
