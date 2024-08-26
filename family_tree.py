import streamlit as st
import pandas as pd
from datetime import datetime

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

    # Sidebar for navigation
    section = st.sidebar.selectbox("Select a section", ["Chores", "Meal Plan", "Tasks", "Reminders", "Health Monitor", "Calendar"])

    # Date selector
    selected_date = st.sidebar.date_input("Select a date", datetime.today())

    # Dictionary to hold the data
    data = {
        "chores": [],
        "meal_plan": [],
        "tasks": [],
        "reminders": [],
        "health_monitor": []
    }

    # Helper function to add, edit, delete entries and update status
    def manage_entries(entry_type):
        st.header(f"{entry_type.capitalize()} for {selected_date}")
        
        if entry_type not in data:
            data[entry_type] = []
        
        # Show existing entries with date, time, and status
        for i, entry in enumerate(data[entry_type]):
            status = "✅" if entry['status'] == "Completed" else "❌"
            st.write(f"{entry['description']} - {entry['time']} ({entry['date']}) - Status: {status}")
            
            if st.button(f"Mark as Completed - {entry['description']}", key=f"complete_{entry_type}_{i}"):
                entry['status'] = "Completed"
                st.success(f"{entry_type.capitalize()} marked as completed!")
                
            if entry_type == "tasks" and entry['status'] == "Completed":
                if st.button(f"Claim Reward - {entry['description']}", key=f"reward_{entry_type}_{i}"):
                    st.success(f"Reward claimed for completing {entry['description']}!")

            if st.button(f"Delete {entry['description']}", key=f"del_{entry_type}_{i}"):
                data[entry_type].pop(i)
        
        # Add a new entry   
        st.subheader(f"Add new {entry_type}")
        description = st.text_input(f"{entry_type.capitalize()} description")
        time = st.time_input(f"Time for the {entry_type}")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if st.button(f"Add {entry_type}"):
            data[entry_type].append({
                "description": description, 
                "time": time.strftime("%H:%M"),
                "date": current_time,
                "status": "Pending"
            })
            st.success(f"{entry_type.capitalize()} added!")

    if section == "Chores":
        manage_entries("chores")
    elif section == "Meal Plan":
        st.header(f"Meal Plan for {selected_date}")
        st.subheader("Meal Ideas")
        meal_ideas = ["Pancakes", "Salad", "Pasta", "Soup", "Grilled Chicken"]
        st.write(", ".join(meal_ideas))

        manage_entries("meal_plan")
    elif section == "Tasks":
        manage_entries("tasks")
    elif section == "Reminders":
        manage_entries("reminders")
    elif section == "Health Monitor":
        st.header(f"Health Monitor for {selected_date}")
        weight = st.number_input("Weight (kg)", min_value=0, step=1)
        sleep_hours = st.number_input("Sleep (hours)", min_value=0, step=1)
        if st.button("Save Health Data"):
            data["health_monitor"].append({
                "weight": weight,
                "sleep_hours": sleep_hours,
                "date": selected_date.strftime("%Y-%m-%d")
            })
            st.success("Health data saved!")
        
        if data["health_monitor"]:
            st.subheader("Health Data")
            df = pd.DataFrame(data["health_monitor"])
            st.table(df)
        
    elif section == "Calendar":
        st.header("Calendar")
        # For now, display a simple text
        st.write("Calendar view to be implemented...")

    # Reminder Notification (Placeholder)
    if st.sidebar.button("Check for Reminders"):
        st.sidebar.write("🔔 Reminder: Check the tasks for today!")



