"""Streamlit entry point for the original offline Smart Classroom interface."""
import streamlit as st

st.set_page_config(page_title="Умный кабинет информатики", page_icon="🏫", layout="wide")
st.markdown('''<style>
.block-container {padding-top: 1.2rem; max-width: 1500px;}
</style>''', unsafe_allow_html=True)
st.title("🏫 Умный кабинет информатики")
st.caption("Автономная версия сайта в Streamlit")
st.info("По умолчанию сайт работает в режиме симуляции. Связь с ESP32 и LCD требует совместимой прошивки и отдельной проверки.")
st.markdown('[Открыть сайт на весь экран (в том числе для USB)](app/static/index.html)')
st.iframe('/app/static/index.html', height=1800, alt='Панель умного кабинета')
