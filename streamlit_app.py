import requests
import json
import streamlit as st

# Function to call the API and beautify the response
def call_api(inputs):
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # This is your API key
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": "n834YRtN-Sw_lg1U4nZJ7",
            # This field can be omitted to run the latest published version
            "spellVersionId": "7Rix1u6a60fm1Y-vYZM-l",
            "inputs": inputs
        }),
    )

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None

# Streamlit app
def main():
    st.title("Respell AI API Response")

    # Input fields
    st.sidebar.header("Input Fields")
    product_or_service = st.sidebar.text_input("Product or Service", "Example text")
    price = st.sidebar.text_input("Price", "Example text")
    location = st.sidebar.text_input("Location", "Example text")
    name = st.sidebar.text_input("Name", "Example text")
    email = st.sidebar.text_input("Email", "Example text")

    inputs = {
        "product_or_service": product_or_service,
        "price": price,
        "location": location,
        "name": name,
        "email": email,
    }

    # Call the API
    api_response = call_api(inputs)

    if api_response:
        # Beautify the response
        for key, value in api_response.items():
            st.write(f"**{key}:** {value}")
    else:
        st.error("Failed to fetch API response")

if __name__ == "__main__":
    main()
