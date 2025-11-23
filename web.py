import streamlit as st
import functions

todos = functions.get_todos()

st.title('My To-Do App')
st.subheader('This app will make your life easy!')
st.write('This app is to increase your productivity!')

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Write a new todo:")

print("Hello")