import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Lundeen", page_icon=None, initial_sidebar_state="auto", layout="wide"
)

st.image("app/images/family_pic.jpeg")
st.title("The Lundeen Foundation")

st.markdown(
    """
Welcome to the Lundeen Foundation page! This is where you can find all information pertaining the the Lundeen family reunion, acitivies, surveys as well as sign ups. 


### Where do I find the pages?
You can access these services using the expandable side bar on the left. If you don't already see it, look for an arrow that looks like " > " and click/touch it to expand the sidebar.


"""
)
