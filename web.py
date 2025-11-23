import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title('My To-Do App')
st.subheader('This app will make your life easy!')
st.write('This app is to increase your productivity!')

for todo in todos:
    st.checkbox(todo)

st.text_input(" ", placeholder="Write a new todo:", on_change=add_todo, key="new_todo")

print("Hello")
