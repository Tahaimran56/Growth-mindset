import streamlit as st
import random

st.title("hello everyone😍")
st.write("i am taha qureshi and this is my simple  project...🤓🤓")

st.title("Growth Mindset App 🌱")
st.write("Welcome! Let’s nurture a positive mindset step by step. 🚀")

affirmations = [
    "I am capable of learning anything I set my mind to.",
    "Mistakes help me grow and improve.",
    "Challenges are opportunities to become stronger.",
    "I believe in my ability to figure things out.",
    "Every day, I am becoming the best version of myself."
]

if st.button("Get a Daily Affirmation ?"):
    st.success(random.choice(affirmations))


st.header("Set a Small Goal 🎯")
goal = st.text_input("What’s one small goal you want to achieve today?")
if goal:
    st.write(f"🌟 Your Goal: {goal}")

st.header("Reflect on Your Day 📝")
reflection = st.text_area("Write a few thoughts, wins, or lessons you learned today:")


if st.button("Save Reflection"):
    st.write("✅ Reflection saved! Take a moment to appreciate your growth.")

if st.button("Clear Reflection"):
    reflection = ""
    st.write("🧹 Reflection cleared. Ready for a fresh start!")


st.write("Remember: Growth is a journey, not a destination. Keep going! 🌻")



st.text(" all the best for ur future🥰")