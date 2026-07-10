import streamlit as st

st.title("My Demo App")


name = st.text_input("Enter name: ")
username = st.text_input("Enter username: ")
email = st.text_input("Enter email: ")
password = st.text_input("Enter password ")
mob = st.text_input("Enter mob : ")

if st.button("Submit"):
    st.write( f"Hello {name}, {username}" )

for x in range(3):
    st.spinner(f"Loop is running for the {x} time.")
