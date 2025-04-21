import streamlit as st
from gtts import gTTS
import speech_recognition as sr
import os

# Sidebar for extra information and controls
st.sidebar.title("Chatbot Assistant")
st.sidebar.info("This is a simple chatbot that assists you with various tasks.")

# Header Section
st.markdown("# Welcome to the Chatbot Assistant :speech_balloon:")
st.markdown("**How can I help you today?**")

# User input section
user_input = st.text_input("Type your message:")

if st.button("Send"):
    if user_input:
        st.write(f"**User**: {user_input}")
        st.write("**Chatbot**: How can I assist you further?")
    else:
        st.warning("Please type a message before sending.")

# Adding voice input feature (using Speech Recognition)
st.markdown("### You can also speak to the assistant :microphone:")
if st.button("Start Speaking"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening for your speech...")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"**You said**: {text}")
            st.write("**Chatbot**: How can I assist you further?")
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your speech.")
        except sr.RequestError:
            st.error("Sorry, there was an issue with the speech recognition service.")

# Chatbot speech output using Text-to-Speech (gTTS)
if user_input:
    tts = gTTS(text=f"How can I assist you further with {user_input}?", lang='en')
    tts.save("chatbot_response.mp3")
    audio_file = open("chatbot_response.mp3", "rb")
    st.audio(audio_file)

# Display Progress Bar (optional)
st.progress(50)  # Example progress bar

# Adding success and info alerts
st.success("Chatbot is up and running!")
st.info("You can send messages or use voice input.")

# File upload feature (optional)
uploaded_file = st.file_uploader("Upload a file to analyze")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Clean up the generated audio file
if os.path.exists("chatbot_response.mp3"):
    os.remove("chatbot_response.mp3")
