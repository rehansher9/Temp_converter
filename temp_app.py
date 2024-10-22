import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def temperature_converter():
    st.title("🌡️ Temperature Converter")

    # Add a sidebar with some extra information
    st.sidebar.title("Temperature Conversion Guide")
    st.sidebar.write("This app converts temperatures between Celsius and Fahrenheit.")
    st.sidebar.markdown("### Conversion Formulas:")
    st.sidebar.write("- **Celsius to Fahrenheit**: (°C × 9/5) + 32 = °F")
    st.sidebar.write("- **Fahrenheit to Celsius**: (°F − 32) × 5/9 = °C")

    # Add a cool title with emojis
    st.subheader("Select the type of conversion:")

    # Dropdown to select conversion type
    conversion_type = st.radio("Choose the conversion type", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

    # Interactive temperature input using a slider or number input depending on user choice
    if conversion_type == "Celsius to Fahrenheit":
        celsius = st.slider("Select the temperature in Celsius", min_value=-100.0, max_value=100.0, step=0.1)
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"🌡️ {celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
        st.balloons()  # Add some fun balloons when conversion happens
    
    elif conversion_type == "Fahrenheit to Celsius":
        fahrenheit = st.slider("Select the temperature in Fahrenheit", min_value=-148.0, max_value=212.0, step=0.1)
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"🌡️ {fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
        st.snow()  # Add a fun snow effect

    # Display a helpful message with examples for the user
    st.info("For accurate readings, input the temperature using the sliders above.")

# Run the app
if __name__ == "__main__":
    temperature_converter()
