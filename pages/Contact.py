import streamlit as st
import email_password


st.header("Contact me")

with st.form(key = 'email_forms'):
    user_email = st.text_input("Enter your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    if button:
        email_password.send_email(user_email, message)
    else:
        print("wrong email")
