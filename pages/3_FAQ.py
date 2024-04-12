import streamlit as st

def faq():
    st.header("📖 FAQ")
    faq_text = """
    #### 1. How do I start generating an IEP paragraph?
    To begin, select the section of the IEP you want to work on from the top menu. Enter the student's information into the input fields that appear, such as name, grade, and specific characteristics or observations. Once all necessary fields are filled, click the "Generate Paragraph" button for that section.

    #### 2. What should I do if I notice an error after generating a paragraph?
    If there's an error or something needs to be changed in the generated paragraph, simply modify the inputs as needed and regenerate the paragraph. Make sure to double-check the data entered for accuracy before regenerating.

    #### 3. Can I save a paragraph to modify it later?
    Currently, the application does not support saving paragraphs directly within the interface. However, you can copy the paragraph to your clipboard and paste it into a document or note-taking app for later editing.

    #### 4. What happens if the application does not copy the paragraph to the clipboard?
    If the "Copy to Clipboard" feature fails, you may manually select the text of the paragraph, right-click, and choose "Copy," or use the keyboard shortcut Ctrl+C (Cmd+C on Mac) to copy the text.

    #### 5. How can I ensure that the generated paragraphs fully comply with district guidelines?
    While the application provides a framework for paragraph generation, it's important to review the output to ensure compliance with specific district guidelines and policies. Adjust the templates as necessary to meet local requirements.

    #### 6. Can I customize the templates for different students or needs?
    The templates are predefined, but you can modify the generated text before finalizing the document. If you need more dynamic customization, consider discussing with a developer to enhance the application's functionality.

    #### 7. Is there a way to input data for multiple students at once?
    The current version of the application handles one student at a time. For handling multiple students, you would need to complete the process separately for each student or consider batch processing features in future updates.

    #### 8. Are there any privacy concerns with entering student information into this application?
    Always ensure that the application complies with privacy laws and school policies regarding student data. Discuss with your administrator or IT department about any concerns regarding data handling and privacy.
    """
    st.markdown(faq_text)
