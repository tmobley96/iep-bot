import streamlit as st
import datetime
import pyperclip
import time

# Set page title and layout
st.set_page_config(page_title="IEP Paragraph Generator", page_icon="🎓", layout="centered")

# Function to generate paragraph for each section
def generate_paragraph(section, inputs):
    if section == "Strengths of the student":
        return f"{inputs['name']} will be in the {inputs['grade']} for the upcoming school year {inputs['school_year']}. {inputs['name']} is {inputs['personality_traits']}. {inputs['gender'][0]}{inputs['short_obs_sentences']}. {inputs['name']}'s {inputs['teacher_name']} completed a Teacher IEP Input Survey and reported the following. {inputs['name']} academic strengths are in the area of {inputs['strengths_from_survey']}. {inputs['name']} works well on {inputs['works_well_from_survey']}. {inputs['name']} {inputs['struggles_from_survey']}. While in class, {inputs['name']} {inputs['positives_from_survey']}"
    elif section == "Parental concerns for enhancing the education":
        if inputs['survey_returned']:
            return f"A parent survey was completed on {inputs['survey_date']} by {inputs['name']}'s {inputs['guardian']}, {inputs['guardian_name']}. They feel that {inputs['name']} strengths are in: {inputs['strengths_from_survey']}. {inputs['gender'][0]} is weak in the area of: {inputs['weakness_from_survey']}. {inputs['gender'][0]} learns best {inputs['best_practice_from_survey']}. While at home, {inputs['name']} {inputs['activities_from_survey']}"
        else:
            return "A parent inventory survey was sent home, but was not returned."
    elif section == "Student Preferences and/or Interests":
        return f"According to the Student Survey completed on {inputs['survey_date']}, {inputs['name']} stated that {inputs['gender'][0]}{inputs['likes_to_do']}. {inputs['gender'][0]} {inputs['enjoys_to_do']}.  {inputs['favorite_subjects'][0]} is her favorite subject. {inputs['gender'][0]} {inputs['delighted_to_do']}. According to {inputs['name']}, {inputs['gender'][0]} is {inputs['student_downfalls']}. {inputs['gender'][0]} {inputs['learns_best']}."
    elif section == "Results of the most recent evaluations":
        return f"{inputs['name']} was given the {inputs['test_name']} on {inputs['test_date']} and achieved the following standards, age, and grade equivalent scores:\nAge equivalent scores:\nMath Concepts and Applications: {inputs['math_concept_score']}\nLetter and Word Recognition: {inputs['letter_word_score']}\nReading Comprehension: {inputs['reading_comprehension_score']}\nMath Computation: {inputs['math_computation_score']}\nWhen scored on grade norms achieved the following standard scores and grade equivalencies:\nMath Concepts and Applications: {inputs['math_concept_norm']}\nLetter and Word Recognition: {inputs['letter_word_norm']}\nReading Comprehension: {inputs['reading_comprehension_norm']}\nMath Computation: {inputs['math_computation_norm']}\n{inputs['name']} took the STAR Reading on {inputs['star_reading_date']} and STAR Math on {inputs['star_math_date']} and achieved the following results:\nSTAR Reading -  Scaled score {inputs['star_reading_score']} which places her in the {inputs['range_name_read']} range; oral reading fluency of {inputs['words_per_minute']} which means {inputs['gender'][0]} can likely read {inputs['words_per_minute']} words per minute on grade level appropriate text.\nSTAR Math - Scaled score {inputs['star_math_score']} which places her in the {inputs['range_name_math']} range; grade equivalent {inputs['grade_equivalent_score']} which is comparable to that of an average {inputs['compare_grade']} grader after the {inputs['compare_month']} month of the school year."
    elif section == "The Academic, Developmental, and Functional Needs of the Student":
        return f"{inputs['name']} is performing {inputs['subject_performance']} in {inputs['subject']}. {inputs['name']} has a more difficult time with {inputs['comprehension_difficulty']} comprehension questions. {inputs['name']}'s performance within content areas is {inputs['content_area_performance']} when reading and math is within {inputs['gender'][1]} grade level. {inputs['gender'][0]} had {inputs['fluency_levels']} and has difficulty {inputs['new_material_comprehension']}. {inputs['gender'][0]} continues to {inputs['reading_math_struggle']}, and difficulties with understanding what {inputs['gender'][0]} has read. {inputs['gender'][0]} {inputs['listening_comprehension']} and this improves {inputs['gender'][1]} reading comprehension. {inputs['gender'][0]} is able to {inputs['general_comprehension']} most of the time. {inputs['name']} can {inputs['add_subtract_skills']}. When solving word problems {inputs['gender'][0]} does {inputs['word_problem_assistance']}. {inputs['name']} still {inputs['multiplication_facts']}. {inputs['name']} will need to receive {inputs['instruction_needs']}. When {inputs['name']} is provided with {inputs['accommodations_success']}."

# Create sections for each part of the IEP
sections = [
    "Strengths of the student",
    "Parental concerns for enhancing the education",
    "Student Preferences and/or Interests",
    "Results of the most recent evaluations",
    "The Academic, Developmental, and Functional Needs of the Student"
]

paragraphs = {}

for section in sections:
    st.header(section)
    
    # Create input fields for user data based on variables
    inputs = {}
    
    if section == "Strengths of the student":
        inputs["name"] = st.text_input("Name (First Name only)")
        inputs["gender"] = st.radio("Gender", ["he, him, his", "she, her, hers"])
        inputs["grade"] = st.selectbox("Grade", ["Kindergarden", "First Grade", "Second Grade", "Third Grade", "Fourth Grade", "Fifth Grade"])
        inputs["school_year"] = st.text_input("School Year (20XX/20XX format)")
        inputs["personality_traits"] = st.text_input("3 Personality Traits (comma-separated)")
        inputs["short_obs_sentences"] = st.text_input("2 Short Observation Sentences")
        inputs["teacher_name"] = st.text_input("Teacher's Last Name")
        inputs["strengths_from_survey"] = st.text_input("Student's Listed Strengths from Teacher Survey")
        inputs["works_well_from_survey"] = st.text_input("Student Works Wells from Teacher Survey")
        inputs["struggles_from_survey"] = st.text_input("Student Struggles from Teacher Survey")
        inputs["positives_from_survey"] = st.text_input("Positives and Strengths from Teacher Survey")
    elif section == "Parental concerns for enhancing the education":
        inputs["survey_returned"] = st.checkbox("Parent Survey Returned")
        if inputs["survey_returned"]:
            inputs["survey_date"] = st.date_input("Date Parental Survey Returned")
            inputs["guardian"] = st.selectbox("Guardian", ["Mother", "Father", "Grandmother", "Grandfather"])
            inputs["guardian_name"] = st.text_input("Guardian Name (First Name only)")
            inputs["strengths_from_survey"] = st.text_input("Strengths of Student from Survey")
            inputs["weakness_from_survey"] = st.text_input("Weakness of Student from Survey")
            inputs["best_practice_from_survey"] = st.text_input("Best Practices of Student from Survey")
            inputs["activities_from_survey"] = st.text_input("Favorite Activities of Student from Survey")
    elif section == "Student Preferences and/or Interests":
        inputs["survey_date"] = st.date_input("Date Student Survey Completed")
        inputs["likes_to_do"] = st.text_input("What the Student Likes to Do from Survey")
        inputs["enjoys_to_do"] = st.text_input("What the Student Enjoys to Do from Survey")
        inputs["favorite_subjects"] = st.text_input("Two of Student's Favorite Subjects from Survey (comma-separated)")
        inputs["delighted_to_do"] = st.text_input("Last of Student's Favorite Subject from Survey")
        inputs["student_downfalls"] = st.text_input("What the Student Believes They Struggle At")
        inputs["learns_best"] = st.text_input("What the Student Believes How They Learn Best")
    elif section == "Results of the most recent evaluations":
        inputs["test_name"] = st.text_input("Name of Test Given")
        inputs["test_date"] = st.date_input("Date of Test Given")
        inputs["math_concept_score"] = st.text_input("Math Concepts and Applications Scores")
        inputs["letter_word_score"] = st.text_input("Letter and Word Recognition Scores")
        inputs["reading_comprehension_score"] = st.text_input("Reading Comprehension Scores")
        inputs["math_computation_score"] = st.text_input("Math Computation Scores")
        inputs["math_concept_norm"] = st.text_input("Math Concepts and Applications Norm")
        inputs["letter_word_norm"] = st.text_input("Letter and Word Recognition Norm")
        inputs["reading_comprehension_norm"] = st.text_input("Reading Comprehension Norm")
        inputs["math_computation_norm"] = st.text_input("Math Computation Norm")
        inputs["star_reading_date"] = st.date_input("Date STAR Reading Test was Taken")
        inputs["star_math_date"] = st.date_input("Date STAR Math Test was Taken")
        inputs["star_reading_score"] = st.number_input("Score of STAR Reading Test", value=0, step=1)
        inputs["range_name_read"] = st.text_input("Range Placement Based on STAR Reading Test Score")
        inputs["words_per_minute"] = st.number_input("How Many Words Per Minute Can the Student Read At", value=0, step=1)
        inputs["star_math_score"] = st.number_input("Score of STAR Math Test", value=0, step=1)
        inputs["range_name_math"] = st.text_input("Range Placement Based on STAR Math Test Score")
        inputs["grade_equivalent_score"] = st.text_input("Grade Equivalent Based on STAR Math Test Score")
        inputs["compare_grade"] = st.selectbox("Grade at Which Student Compares Based on STAR Math Test Score", ["first", "second", "third", "fourth", "fifth"])
        inputs["compare_month"] = st.selectbox("Month of Grade at Which Student Compares Based on STAR Math Test Score", ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"])
    elif section == "The Academic, Developmental, and Functional Needs of the Student":
        inputs["subject_performance"] = st.text_input("Description of Student's Reading Performance Compared to Grade Level")
        inputs["subject"] = st.text_input("Subject")
        inputs["comprehension_difficulty"] = st.text_input("Description of Student's Difficulty with Specific Types of Comprehension Questions")
        inputs["content_area_performance"] = st.text_input("Description of How Student's Performance in Content Areas is Affected by Reading and Math Skills")
        inputs["fluency_levels"] = st.text_input("Description of Student's Fluency Levels")
        inputs["new_material_comprehension"] = st.text_input("Description of Student's Difficulty Comprehending New Material")
        inputs["reading_math_struggle"] = st.text_input("Description of Student's Struggles in Reading and Math")
        inputs["listening_comprehension"] = st.text_input("Description of Student's Listening Comprehension Skills and How They Affect Reading Comprehension")
        inputs["general_comprehension"] = st.text_input("Description of Student's General Ability to Comprehend What They Read")
        inputs["add_subtract_skills"] = st.text_input("Description of Student's Ability to Add and Subtract Without Regrouping")
        inputs["word_problem_assistance"] = st.text_input("Description of Student's Need for Assistance When Solving Word Problems")
        inputs["multiplication_facts"] = st.text_input("Description of Student's Struggles with Multiplication Facts")
        inputs["instruction_needs"] = st.text_input("Description of the Type of Instruction the Student Needs to Ensure Remediation and Retention of Skills")
        inputs["accommodations_success"] = st.text_input("Description of How the Student Performs When Provided with Accommodations and Access to the Resource Room")
    
    if st.button(f"Generate Paragraph for {section}"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        paragraph = generate_paragraph(section, inputs)
        paragraphs[section] = paragraph
        
        st.text_area(f"Generated Paragraph for {section}", value=paragraph, height=200)
        if st.button(f"Copy {section} Paragraph to Clipboard"):
            pyperclip.copy(paragraph)
            st.success("Paragraph copied to clipboard!")

if st.button("Generate Full IEP"):
    progress_bar = st.progress(0)
    full_iep = ""
    for section in sections:
        paragraph = generate_paragraph(section, paragraphs.get(section, {}))
        full_iep += f"**{section}**\n{paragraph}\n\n"
        progress_bar.progress((sections.index(section) + 1) / len(sections))
    
    st.text_area("Full IEP", value=full_iep, height=500)
    if st.button("Copy Full IEP to Clipboard"):
        pyperclip.copy(full_iep)
        st.success("Full IEP copied to clipboard!")

st.markdown("---")
st.text("IEP Paragraph Generator v1.0")


# import streamlit as st
# import time
# from datetime import datetime

# # Set page title and layout
# st.set_page_config(page_title="IEP Paragraph Generator", page_icon="🎓", layout="centered")

# # Page title
# st.title("IEP Paragraph Generator")

# # Input fields for user data
# date_survey_sent = st.date_input("Date Parental Survey Was Sent Out")
# survey_not_returned = st.checkbox("Survey Not Returned")

# date_survey_returned = st.date_input("Date Parental Survey Returned", disabled=survey_not_returned)
# guardian = st.text_input("Guardian", value="Parent/Guardian", disabled=survey_not_returned)
# guardian_name = st.text_input("Guardian Name", value="Full Name", disabled=survey_not_returned)
# student_strengths = st.text_input("Student Strengths", value="List strengths here", disabled=survey_not_returned)
# student_weaknesses = st.text_input("Student Weaknesses", value="List weaknesses here", disabled=survey_not_returned)
# best_practices = st.text_input("Best Practices", value="List best practices here", disabled=survey_not_returned)
# activities = st.text_input("Activities", value="List activities here", disabled=survey_not_returned)

# # Generate Paragraph button
# if st.button("Generate Paragraph"):
#     # Display progress bar
#     progress_bar = st.progress(0)
#     for i in range(100):
#         time.sleep(0.02)
#         progress_bar.progress(i + 1)

#     # Format dates
#     formatted_date_survey_sent = date_survey_sent.strftime("%B %d, %Y")
#     formatted_date_survey_returned = date_survey_returned.strftime("%B %d, %Y")

#     # Generate paragraph
#     if survey_not_returned:
#         paragraph = f"The parental survey was sent out on {formatted_date_survey_sent}, but it was not returned."
#     else:
#         paragraph = f"The parental survey was sent out on {formatted_date_survey_sent} and returned on {formatted_date_survey_returned}. {guardian} {guardian_name} provided the following information about the student: Strengths: {student_strengths}. Weaknesses: {student_weaknesses}. Best practices for working with the student include: {best_practices}. Activities the student enjoys include: {activities}."

#     # Display generated paragraph
#     st.subheader("Generated Paragraph")
#     st.text_area("", value=paragraph, height=200)

#     # Copy to clipboard button
#     if st.button("Copy to Clipboard"):
#         st.code(paragraph)

# # Footer
# st.markdown("---")
# st.markdown("IEP Paragraph Generator v1.5")