import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def temperature_converter():
    st.title("Temperature Converter")

    # Dropdown to select conversion type
    conversion_type = st.selectbox("Choose the conversion type", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

    if conversion_type == "Celsius to Fahrenheit":
        # Input for Celsius temperature
        celsius = st.number_input("Enter temperature in Celsius", format="%.2f")
        # Convert to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    
    elif conversion_type == "Fahrenheit to Celsius":
        # Input for Fahrenheit temperature
        fahrenheit = st.number_input("Enter temperature in Fahrenheit", format="%.2f")
        # Convert to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

# Run the app
if __name__ == "__main__":
    temperature_converter()
