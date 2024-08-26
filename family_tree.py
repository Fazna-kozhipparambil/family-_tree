import streamlit as st
import pandas as pd
from datetime import datetime


# Add custom CSS for styling
st.markdown("""
<style>
.header {
    font-size: 2em;
    color: #FF6347;
    text-align: center;
}
.container {
    display: flex;
    justify-content: space-around;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Your existing Streamlit code
st.title("Family Tree Planner")


# Set up the page configuration
st.set_page_config(page_title="Family Tree", layout="wide")

# User credentials (in a real app, you would store and handle these securely)
USER_CREDENTIALS = {"parent1": "password1", "parent2": "password2"}

# Function to handle login
def login(username, password):
    if USER_CREDENTIALS.get(username) == password:
        return True
    return False

# Login section
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.sidebar.success("Logged in successfully!")
        else:
            st.sidebar.error("Invalid username or password")
else:
    st.sidebar.success("You are logged in!")
    
    # Title of the app
    st.title('Family Tree')
    
from datetime import datetime

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select a section:",
    ["Home", "Household Chores", "Meal Plan", "Daily Tasks", "Health Monitor", "Calendar"]
)

# Define initial data for demo purposes
if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=["Task", "Priority", "Status", "Assigned To"])

if 'chores' not in st.session_state:
    st.session_state.chores = pd.DataFrame(columns=["Chore", "Assigned To"])

if 'meals' not in st.session_state:
    st.session_state.meals = pd.DataFrame(columns=["Meal", "Day"])

# Main content based on selected option
if option == "Home":
    st.header("Welcome to the Family Tree Planner")
    st.write("Manage your family's daily routines, meals, tasks, and more.")

elif option == "Household Chores":
    with st.expander("Household Chores"):
        st.header("Household Chores")
        with st.form(key='chores_form'):
            chore = st.text_input("Chore Description")
            assigned_to = st.text_input("Assign To")
            submit_button = st.form_submit_button("Add Chore")
            if submit_button:
                st.session_state.chores = st.session_state.chores.append({"Chore": chore, "Assigned To": assigned_to}, ignore_index=True)
                st.write(f"Chore Added: {chore} for {assigned_to}")
        st.dataframe(st.session_state.chores)

elif option == "Meal Plan":
    with st.expander("Meal Plan"):
        st.header("Meal Plan")
        with st.form(key='meal_form'):
            meal = st.text_input("Meal Description")
            day = st.text_input("Day of the Week")
            submit_button = st.form_submit_button("Add Meal")
            if submit_button:
                st.session_state.meals = st.session_state.meals.append({"Meal": meal, "Day": day}, ignore_index=True)
                st.write(f"Meal Added: {meal} for {day}")
        st.dataframe(st.session_state.meals)

elif option == "Daily Tasks":
    with st.expander("Daily Tasks"):
        st.header("Daily Tasks")
        with st.form(key='tasks_form'):
            task = st.text_input("Task Description")
            priority = st.slider("Priority", 1, 10)
            assigned_to = st.text_input("Assign To")
            status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
            submit_button = st.form_submit_button("Add Task")
            if submit_button:
                st.session_state.tasks = st.session_state.tasks.append({
                    "Task": task, 
                    "Priority": priority, 
                    "Status": status, 
                    "Assigned To": assigned_to
                }, ignore_index=True)
                st.write(f"Task Added: {task} with Priority {priority} for {assigned_to}")
        st.dataframe(st.session_state.tasks)

elif option == "Health Monitor":
    with st.expander("Health Monitor"):
        st.header("Health Monitor")
        st.write("Health monitoring features will be here.")
        # Add any health monitoring code or placeholders here

elif option == "Calendar":
    with st.expander("Calendar"):
        st.header("Calendar")
        st.write(f"Today's date: {datetime.now().strftime('%Y-%m-%d')}")
        # Implement calendar functionality here or use Streamlit's date input
        date_selected = st.date_input("Select a date", datetime.now())
        st.write(f"Selected date: {date_selected}")

# Additional: Rewards System for Kids (Placeholder)
with st.sidebar.expander("Rewards System"):
    if st.session_state.tasks.shape[0] > 0:
        completed_tasks = st.session_state.tasks[st.session_state.tasks["Status"] == "Completed"]
        if len(completed_tasks) > 0:
            st.write(f"Number of tasks completed: {len(completed_tasks)}")
            st.write("Rewards can be set based on the number of completed tasks.")

# Footer
st.markdown("""
<style>
.header {
    font-size: 2em;
    color: #FF6347;
    text-align: center;
}
.container {
    display: flex;
    justify-content: space-around;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

