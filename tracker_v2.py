import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="FocusTrack", layout="centered")

# Load data
if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
else:
    df = pd.DataFrame(columns=["Task", "Duration (min)", "Date"])

st.title("🧠 FocusTrack")

menu = st.sidebar.selectbox("Menu", ["Tracker", "Dashboard"])

if menu == "Tracker":
    st.subheader("Track Your Session")
    task = st.text_input("Task Name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    if st.button("Save"):
        new_data = pd.DataFrame([[task, duration, pd.Timestamp.now().strftime("%Y-%m-%d")]],
                                columns=["Task", "Duration (min)", "Date"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv("data.csv", index=False)
        st.success("Saved successfully!")

elif menu == "Dashboard":
    st.subheader("Your Productivity Dashboard")
    if df.empty:
        st.info("No data yet — start tracking!")
    else:
        total_time = df["Duration (min)"].sum()
        st.metric("Total Focus Time (min)", total_time)
        st.bar_chart(df.groupby("Date")["Duration (min)"].sum())
        st.dataframe(df)

st.caption("Built with ❤️ using rexrain")




