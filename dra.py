import streamlit as st
from datetime import datetime, timedelta

# Title
st.title("Daily Reminder App")

# Subtitle
st.subheader("Stay on track with your daily tasks!")

# Define daily tasks
tasks = [
    {"task": "Drink Water", "frequency": "Every Hour"},
    {"task": "Brush Teeth", "frequency": "Morning and Night"},
    {"task": "Take a Bath", "frequency": "Once a Day"},
    {"task": "Breakfast", "frequency": "Morning"},
    {"task": "Lunch", "frequency": "Afternoon"},
    {"task": "Dinner", "frequency": "Evening"},
    {"task": "Eat Snacks", "frequency": "Twice a Day"},
]

# Task checklist
st.header("Task Checklist")
for task in tasks:
    st.checkbox(f"{task['task']} - {task['frequency']}")

# Reminders section
st.header("Upcoming Reminders")
current_time = datetime.now()
time_format = "%I:%M %p"

reminders = [
    {"task": "Drink Water", "time": current_time + timedelta(minutes=60)},
    {"task": "Brush Teeth", "time": current_time.replace(hour=7, minute=0)},
    {"task": "Take a Bath", "time": current_time.replace(hour=9, minute=0)},
    {"task": "Breakfast", "time": current_time.replace(hour=8, minute=0)},
    {"task": "Lunch", "time": current_time.replace(hour=13, minute=0)},
    {"task": "Dinner", "time": current_time.replace(hour=20, minute=0)},
    {"task": "Eat Snacks", "time": current_time.replace(hour=16, minute=0)},
]

for reminder in reminders:
    if reminder["time"] > current_time:
        st.write(f"**{reminder['task']}**: {reminder['time'].strftime(time_format)}")

# Log activity
st.header("Log Your Activities")
if "activity_log" not in st.session_state:
    st.session_state.activity_log = []

if st.button("Log Current Time"):
    st.session_state.activity_log.append(datetime.now().strftime("%Y-%m-%d %I:%M %p"))
    st.success("Activity logged!")

st.write("### Activity Log:")
if st.session_state.activity_log:
    for log in st.session_state.activity_log:
        st.write(f"- {log}")
else:
    st.write("No activities logged yet.")

# Footer
st.write("---")
st.caption("Built with ❤️ using Streamlit")
