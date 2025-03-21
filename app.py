import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":basketball:", layout="centered")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("Style/style.css")



# ----- Header Section ----- #
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Martin :wave:")
        st.title("An aspiring software developer")
        st.write("I like learning about python!!")
    with right_column:
        st.image("Capture.PNG")
    
with st.container():
    st.write("---")
    st.header("What I do")
    st.write("##")
    st.write(
        """
            Hi my name is Martin, I come from Serbia and i really enjoy programming.    
        """              
        )
    st.write("##")
        
    # --- CONTACT --- #
    with st.container():
        st.write("")
        st.header("Get In Touch With Me")
        contact_form = """
        <input type="hidden" name="_captcha" value="false">
        <form action="https://formsubmit.co/crki73@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your e-mail" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
        
        
        
        
    
    
    
    
    
    
    