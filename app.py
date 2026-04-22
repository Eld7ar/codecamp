# app.py
import streamlit as st
import chatbot

st.set_page_config(
    page_title="Projectum Assistant",
    page_icon="🎓",
    layout="centered"
)

chatbot.app()
