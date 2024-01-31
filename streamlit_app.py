import streamlit as st

def main():
    st.write("<h1>My Chat App</h1>", unsafe_allow_html=True)
    # Render the chat script using Streamlit's html component
    st.write(
        f'<script src="https://webgpt.getvideowhizz.com/chat/chat.js" id="217" user_id="11" app="skillpayai"></script>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
