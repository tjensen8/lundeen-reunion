import streamlit as st
import pandas as pd

st.title("Schedule")

st.markdown(
    """
Here you can find the current schedule of events!
"""
)

schedule = pd.DataFrame(
    {
        "Date": ["07-10-1993", "07-10-1993", "07-11-1993"],
        "Start Time": ["8 AM", "9 AM", "3 PM"],
        "End Time": ["10 AM", "11 AM", "4 PM"],
        "Activity Name": ["Breakfast", "Yoga", "Hide and Seek"],
        "Sponsor": ["Brian Jensen", "Karen Jensen", "Taylor Jensen"],
    }
)

# group by date
schedule_by_date = schedule.groupby("Date")

# st.write(schedule_by_date.groups)

for date in schedule_by_date.grouper:
    # with st.expander(label=date):
    with st.container():
        st.title(date)
        st.dataframe(schedule_by_date.get_group(date))
    # st.dataframe(schedule)
