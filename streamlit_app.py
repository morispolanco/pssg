import streamlit as st
import requests
import json

def spell_call(spellId, spellVersionId, inputs):
    """Makes a POST request to the Respell.ai API to run a spell.

    Args:
    spellId: The ID of the spell to run.
    spellVersionId: The ID of the spell version to run.
    inputs: A dictionary of input values for the spell.

    Returns:
    A dictionary containing the spell output.
    """

    # Set the API endpoint and headers
    api_endpoint = "https://api.respell.ai/v1/run"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    # Prepare the request data
    data = {
        "spellId": spellId,
        "spellVersionId": spellVersionId,
        "inputs": inputs,
    }

    # Make the POST request
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

    # Return the spell output
    return response.json()

def main():
    st.title("Respell.ai Spell Runner")

    # Get the spell ID and spell version ID from the user
    spell_id = st.text_input("Spell ID")
    spell_version_id = st.text_input("Spell Version ID")

    # Get the input values from the user
    product_or_service = st.text_input("Product or service")
    price = st.text_input("Price")
    location = st.text_input("Location")
    name = st.text_input("Name")
    email = st.text_input("Email")

    # Prepare the input values for the spell
    inputs = {
        "product_or_service": product_or_service,
        "price": price,
        "location": location,
        "name": name,
        "email": email,
    }

    # Call the spell
    if st.button("Run Spell"):
        spell_output = spell_call(spell_id, spell_version_id, inputs)
        # Display the spell output
        st.write("Spell output:")
        st.json(spell_output)

if __name__ == "__main__":
    main()
