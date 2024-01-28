import requests
import json
import streamlit as st

# Function to call the API and beautify the response
def call_api():
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # This is your API key
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": "SwM1TRZNvRQjaA-bJ969H",
            # This field can be omitted to run the latest published version
            "spellVersionId": "qHiqa1EwXNP1LNoj9Ow_l",
            # Fill in values for each of your 6 dynamic input blocks
            "inputs": {
                "email": "Example text",
                "name": "Example text",
                "location": "Example text",
                "price": "Example text",
                "product_or_service": "Example text",
                "language_2": "Example text",
            }
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

    # Call the API
    api_response = call_api()

    if api_response:
        st.header("API Response")
        st.json(api_response)
    else:
        st.error("Failed to fetch API response")

if __name__ == "__main__":
    main()
