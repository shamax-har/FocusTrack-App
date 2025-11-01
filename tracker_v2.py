# FocusTrack v2 — Hybrid Dark Premium
# Author: You & your friend 🚀
# Description: Smart productivity + focus tracker with custom & shareable tasks
# Run on Streamlit: https://share.streamlit.io

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FocusTrack v2", page_icon="🌙", layout="wide")

# ---------- Initialize ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = {
        "Study": True,
        "Workout": True,
        "Sleep": True,
        "Gym": True,
        "Mood": True
    }
if "custom_tasks" not in st.session_state:
    st.session_state.custom_tasks = []
if "public_tasks" not in st.session_state:
    st.session_state.public_tasks = list(st.session_state.tasks.keys())

# ---------- Style ----------
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        color: #f0f0f0;
    }
    .main {
        background-color: #0f1117;
    }
    div[data-testid="stSidebar"] {
        background-color: #161a22;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌙 FocusTrack v2 — Hybrid Dark Premium")
st.markdown("Stay consistent. Stay minimal. Share your focus energy ⚡")

# ---------- Add Tasks ----------
st.subheader("🧩 Your Tasks")
cols = st.columns(2)
with cols[0]:
    for task, enabled in st.session_state.tasks.items():
        st.session_state.tasks[task] = st.checkbox(task, value=enabled)

with cols[1]:
    st.markdown("**Add custom tasks:**")
    new_task = st.text_input("Enter new task name")
    if st.button("➕ Add Task"):
        if new_task.strip() != "":
            st.session_state.custom_tasks.append(new_task.strip())
            st.success(f"Task '{new_task}' added!")

if st.session_state.custom_tasks:
    st.markdown("### Your Custom Tasks")
    for task in st.session_state.custom_tasks:
        st.checkbox(task, value=True)

# ---------- Public/Private Options ----------
st.divider()
st.subheader("🌍 Visibility Settings")

public_options = []
all_tasks = list(st.session_state.tasks.keys()) + st.session_state.custom_tasks

for task in all_tasks:
    checked = st.checkbox(f"Make '{task}' public", value=task in st.session_state.public_tasks)
    if checked:
        public_options.append(task)

st.session_state.public_tasks = public_options

# ---------- Save Progress ----------
st.divider()
st.subheader("📅 Log Today’s Progress")

if "data" not in st.session_state:
    st.session_state.data = []

if st.button("Save Progress"):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tasks": [t for t, v in st.session_state.tasks.items() if v],
        "custom_tasks": st.session_state.custom_tasks,
        "public": st.session_state.public_tasks
    }
    st.session_state.data.append(entry)
    st.success("Progress saved successfully ✅")

# ---------- View Logs ----------
if st.session_state.data:
    st.divider()
    st.subheader("📊 History")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

# ---------- Share Section ----------
st.divider()
st.subheader("🔗 Share Public Focus")

shareable_tasks = ", ".join(st.session_state.public_tasks)
st.markdown(f"**Your public focus areas:** {shareable_tasks if shareable_tasks else 'None yet'}")

share_link = f"https://share.streamlit.io/yourusername/focustrack-app"
st.markdown(f"[🌐 View Public Dashboard]({share_link})")

st.caption("Made with ❤️ using Streamlit — FocusTrack v2")

