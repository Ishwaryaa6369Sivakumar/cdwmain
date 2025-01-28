
from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()


def poem_generator_app():

     """
     poem generator app
     
     """

     
    # it's a form , storing text box and submit button
with st.form("Poem generator"):
     
     topic = st.text_input("Enter topic for poem")
     submitted = st.form_submit_button("Submit")
     
     if(submitted):
          response = chain.generate_poem(topic)
          st.info(response)
          

poem_generator_app()