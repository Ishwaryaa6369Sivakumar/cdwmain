import json
import streamlit as st
from dotenv import load_dotenv
import chain 

# Load environment variables
load_dotenv()

def parse_plain_text_response(response):
    """
    Parse the plain string response into structured JSON with MCQs.
    """
    questions = response.split("?")  # Split the string by questions
    mcqs = []
    for question in questions:
        if question.strip():  # Skip empty lines
            q = question.strip() + "?"
            mcqs.append({
                "question": q,
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],  
                "answer": "Option 1"  
            })
    return mcqs


def quiz_generator_app():
    """
    Quiz Generator App
    """
    st.title("🧠 Quiz Generator")
    st.write("Create customized quizzes with multiple-choice answers based on your topic and difficulty level!")

    # Sidebar for topic and difficulty selection
    with st.sidebar:
        st.header("Settings")
        topic = st.selectbox("Select Topic", ["Math", "English", "Science", "History", "General Knowledge"], key="topic_select")
        difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"], key="difficulty_radio")

    # Center area for form
    with st.form("Quiz Generator Form"):
        st.subheader("Generate Your Quiz")
        additional_input = st.text_input("Optional: Add more details (e.g., specific chapters, focus areas)", key="additional_input")
        submitted = st.form_submit_button("Generate Quiz")

    # Handle form submission
    if submitted:
        st.success(f"Generating a {difficulty} quiz on {topic} with multiple-choice options...")
        try:
            # Call the generate_quiz function
            response = chain.generate_quiz(topic, difficulty)

            # If the response is a string, try parsing it
            if isinstance(response, str):
                try:
                    # Attempt to parse the response as JSON
                    response = json.loads(response)
                except json.JSONDecodeError:
                    # Fallback: Parse plain text response into structured data
                    response = parse_plain_text_response(response)

            # Validate response structure
            if not isinstance(response, list):
                raise ValueError("Unexpected response format: Expected a list of questions.")

            # Display the quiz
            with st.expander("View Quiz with Options"):
                for idx, question_data in enumerate(response):
                    # Validate each question's structure
                    if not isinstance(question_data, dict):
                        raise ValueError(f"Invalid question format: {question_data}")
                    if not all(k in question_data for k in ("question", "options", "answer")):
                        raise KeyError(f"Missing keys in question: {question_data}")

                    # Display the question and options
                    st.write(f"**{idx + 1}. {question_data['question']}**")
                    for option in question_data["options"]:
                        st.write(f"- {option}")
                    st.write(f"**Answer:** {question_data['answer']}")

        except ValueError as ve:
            st.error(f"Value Error: {ve}")
        except KeyError as ke:
            st.error(f"Key Error: {ke}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

quiz_generator_app()

# fallback message