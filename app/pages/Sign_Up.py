import streamlit as st
import pandas as pd
from streamlit_modal import Modal


st.title("Sign Up For Activities")


st.markdown(
    """

Here is where you can sign up for all of the activities for the family reunion. You can view the results at the bottom of the page.

"""
)

activities = ["Dancing", "Hiking", "Mountain Sliding", "Other Data"]
activities_desc = [
    "Dance the night away. [Link](www.google.com)",
    "Hike the largest peak and plant a flag for the Lundeen Family. [Link](www.google.com)",
    "Slide down a mountain at breakneck speed and maxmimum safety. [Link](www.google.com) ",
    "Here's where more stuff could go. [Link](www.google.com)",
]

st.markdown("### Activities")
for activity, activity_description in zip(activities, activities_desc):
    st.markdown("____")
    st.markdown(f"##### {activity}")
    st.write(activity_description)

st.markdown("____")
st.title("Actions:")
with st.expander("Add people to activities:"):
    st.title("Make your selections.")
    names_text = st.text_input(
        label="Enter in the first and last names of each of the people you are signing up for (including yourself). \n Separate names with a comma (,)"
    )

    def parse_name_selection(names_text: str):
        names_text_cleaned = str(names_text).split(",")

        for name in names_text_cleaned:
            if " " not in name:
                st.error(
                    f"No first/last name is found in the name '{name}'. Please add a first/last name."
                )

        st.warning(
            f"""You are about to submit names for the following people... is this correct? \n
            {str([name for name in names_text_cleaned])}"""
        )
        return names_text_cleaned

    # clicked = st.button("Submit names", key="button_submit")
    # if clicked:
    #    names_list = parse_name_selection(names_text)
    # st.warning("You are about to submit names for ")

    selected_activities = st.multiselect(label="Activities", options=activities)

    names_list = parse_name_selection(names_text)
    clicked_final = st.button("Submit", key="button_final_submit")

with st.expander("Remove People From Activities"):
    st.write("this is where you remove people from activitiess")

with st.expander("What have I signed up for?"):
    st.multiselect("Names:", options=["taylor jensen", "andrew jensen", "lara jensen"])
    st.write("This is where you can see what you have signed up for...")
    st.download_button("Download my schedule.", data=str("hello"))
