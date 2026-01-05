import streamlit as st
from pydeck.io.html import cdn_picker

print("hello")

dropdown = st.selectbox("Choose a letter grade",["A","B","C","D","F"])
st.write("Your grade is a ", dropdown)