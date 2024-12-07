import streamlit as st

def custom_info(message, color):
    st.markdown(
        f"""
        <div style='background-color: {color}; color: #000; padding: 10px; border-radius: 5px;'>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )