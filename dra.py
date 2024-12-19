import streamlit as st
from datetime import datetime, timedelta
import time
from PIL import Image

# Title with colorful text
st.markdown("<h1 style='color:blue;'>🌟 Daily Reminder App 🌟</h1>", unsafe_allow_html=True)

# Display a motivational image
st.image("https://source.unsplash.com/800x400/?nature,water", caption="Stay Hydrated and Focused!", use_column_width=True)

# Subtitle
st.markdown("<h3 style='color:green;'>Stay on track with your daily tasks!</h3>", unsafe_allow_html=True)

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

# Task checklist with emojis
st.header("Task Checklist")
for task in tasks:
    st.checkbox(f"✅ {task['task']} - {task['frequency']}")

# Display a refreshment audio
st.header("🎵 Refreshment Music")
audio_file = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_file, format="audio/mp3")

# Meditation Timer
st.header("🧘 Meditation Timer")
meditation_duration = st.number_input("Set Meditation Duration (in minutes):", min_value=1, max_value=60, value=10)
if st.button("Start Meditation"):
    st.write("Meditation started... Stay calm and breathe!")
    time.sleep(meditation_duration * 60)  # Pause for the meditation duration
    st.success("Meditation completed! 🎉")

# Study Timer for Exams
st.header("📚 Study Timer")
study_start = st.time_input("Study Start Time", value=datetime.strptime("21:00", "%H:%M").time())
study_end = st.time_input("Study End Time", value=datetime.strptime("00:00", "%H:%M").time())
if st.button("Start Study Timer"):
    current_time = datetime.now().time()
    if study_start <= current_time <= study_end:
        st.write("Focus on your studies! 📖 Timer is running.")
        time.sleep((datetime.combine(datetime.today(), study_end) - datetime.now()).seconds)
        st.success("Study session completed! 🎉")
    else:
        st.warning("It's not time to study yet. Check your study schedule.")

# Task Notifications with Sound
st.header("🔔 Task Notifications")
notification_time = st.time_input("Set a Notification Time", value=datetime.now().time())
if st.button("Set Notification"):
    while True:
        if datetime.now().time() >= notification_time:
            st.balloons()
            st.success("🔔 Reminder: It's time for your next task!")
            break
        time.sleep(1)

# Footer with colorful text
st.markdown("<h3 style='color:purple;'>Built with ❤️ using Streamlit</h3>", unsafe_allow_html=True)