import streamlit as st
from PIL import Image

st.set_page_config(page_title="Blossom Goyal Portfolio", page_icon=":tada:", layout="wide")

# ------- HEADER section ------

st.header("Hey, I am Blossom :wave:")
st.title("Technical Support Specialist")
st.write("I am passionate about learning new devops technologies and stay up-to-date in terms of new features.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.header("Let me introduce myself")
        st.write("##")
        st.write(
            """
            - Experience in deploying and upgrading the client servers and keeping them up to date.
            - Set up databases including MySQL and PostgreSQL using the command line in Linux.
            - Set up DNS and network configurations using Microsoft Azure.
            - Manage server backups and monitoring using AWX and Microsoft Azure.
            - Set up Active Directory and LDAP for the clients.
            - Teamwork mindset and leadership qualities.
            """
        )

    with right_column:
        # Load and display the image
        try:
            image = Image.open("blossom_goyal.jpg")
            st.image(image, caption="Blossom Goyal", width=300)  # Adjust width as needed
        except FileNotFoundError:
            st.write("Image not found. Please ensure 'blossom_goyal.jpg' is in the same directory as this script.")