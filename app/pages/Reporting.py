import streamlit as st
import pandas as pd

if "counter" not in list(st.session_state.keys()):
    st.session_state["counter"] = 0


def add_one():
    st.session_state["counter"] = st.session_state["counter"] + 1


def minus_one():
    st.session_state["counter"] = st.session_state["counter"] - 1


def reset():
    st.session_state["counter"] = 0


st.button("+1", key="+1_button", on_click=add_one)
st.button("-1", key="-1_button", on_click=minus_one)
st.button("reset", key="reset_button", on_click=reset)

st.write(st.session_state.counter)


st.title("Data Set")


schedule = pd.DataFrame(
    {
        "Date": ["07-10-1993", "07-10-1993", "07-11-1993"],
        "Start Time": ["8 AM", "9 AM", "3 PM"],
        "End Time": ["10 AM", "11 AM", "4 PM"],
        "Activity Name": ["Breakfast", "Yoga", "Hide and Seek"],
        "Sponsor": ["Brian Jensen", "Karen Jensen", "Taylor Jensen"],
        "Participant Name": ["Devin Jensen", "Karen Jensen", "Lara Jensen"],
    }
)
st.data_editor(schedule)
st.download_button("Download Information", data=str(schedule))
