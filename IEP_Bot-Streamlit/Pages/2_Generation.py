import streamlit as st
import time
from datetime import datetime

# Set page title and layout
st.set_page_config(page_title="IEP Paragraph Generator", page_icon="🎓", layout="centered")

# Page title
st.title("IEP Paragraph Generator")

# Input fields for user data
date_survey_sent = st.date_input("Date Parental Survey Was Sent Out")
survey_not_returned = st.checkbox("Survey Not Returned")

date_survey_returned = st.date_input("Date Parental Survey Returned", disabled=survey_not_returned)
guardian = st.text_input("Guardian", value="Parent/Guardian", disabled=survey_not_returned)
guardian_name = st.text_input("Guardian Name", value="Full Name", disabled=survey_not_returned)
student_strengths = st.text_input("Student Strengths", value="List strengths here", disabled=survey_not_returned)
student_weaknesses = st.text_input("Student Weaknesses", value="List weaknesses here", disabled=survey_not_returned)
best_practices = st.text_input("Best Practices", value="List best practices here", disabled=survey_not_returned)
activities = st.text_input("Activities", value="List activities here", disabled=survey_not_returned)

# Generate Paragraph button
if st.button("Generate Paragraph"):
    # Display progress bar
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)

    # Format dates
    formatted_date_survey_sent = date_survey_sent.strftime("%B %d, %Y")
    formatted_date_survey_returned = date_survey_returned.strftime("%B %d, %Y")

    # Generate paragraph
    if survey_not_returned:
        paragraph = f"The parental survey was sent out on {formatted_date_survey_sent}, but it was not returned."
    else:
        paragraph = f"The parental survey was sent out on {formatted_date_survey_sent} and returned on {formatted_date_survey_returned}. {guardian} {guardian_name} provided the following information about the student: Strengths: {student_strengths}. Weaknesses: {student_weaknesses}. Best practices for working with the student include: {best_practices}. Activities the student enjoys include: {activities}."

    # Display generated paragraph
    st.subheader("Generated Paragraph")
    st.text_area("", value=paragraph, height=200)

    # Copy to clipboard button
    if st.button("Copy to Clipboard"):
        st.code(paragraph)

# Footer
st.markdown("---")
st.markdown("IEP Paragraph Generator v1.5")