import streamlit as st
import requests
import json

def call_api(api_key, spell_id, spell_version_id, inputs):
    url = 'https://api.respell.ai/v1/run'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "spellId": spell_id,
        "spellVersionId": spell_version_id,
        "inputs": inputs
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    api_key = "260cee54-6d54-48ba-92e8-bf641b5f4805"
    spell_id = "n834YRtN-Sw_lg1U4nZJ7"
    spell_version_id = "TI7gzCPzWyPxRkwWB7FFj"

    st.set_page_config(page_title="Streamlit App", page_icon=":guardsman:", layout="wide")

    st.title("Streamlit App using Respell API")

    product_or_service = st.text_input("Product or Service")
    price = st.text_input("Price")
    location = st.text_input("Location")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Submit"):
        inputs = {
            "product_or_service": product_or_service,
            "price": price,
            "location": location,
            "name": name,
            "email": email
        }
        result = call_api(api_key, spell_id, spell_version_id, inputs)
            # Display the result
    st.subheader("Result:")
    for key, value in result.items():
        st.write(f"{key}: {value}")

if __name__ == "__main__":
    main()
