import streamlit as st
import pandas as pd

# Task 1: Initialize persistent data storage for students
if "students" not in st.session_state:
    st.session_state.students = []

# Task 1: Input student data
st.title("Student Score Manager")

# Inputs for name and score
name = st.text_input("Enter student name:")
score = st.number_input("Enter student score:", min_value=0, max_value=100, step=1)

# Add student to the list when the button is clicked
if st.button("Add Student"):
    if name:  # Ensure name is not empty
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f"Added student: {name} with score: {score}")
    else:
        st.error("Student name cannot be empty!")

# Convert the student list to a DataFrame for display
students_df = pd.DataFrame(st.session_state.students)

# Display the student table if data exists
if not students_df.empty:
    st.subheader("Student Data")
    st.write(students_df)

    # Task 2: Add a slider to filter students by a minimum score
    st.subheader("Filter Students by Minimum Score")
    min_score = st.slider("Minimum Score:", min_value=0, max_value=100, value=0)
    
    # Filter students who meet the minimum score criterion
    filtered_df = students_df[students_df["Score"] >= min_score]
    st.write(filtered_df)
else:
    st.info("No student data available. Add students to see the table.")

