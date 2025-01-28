from model import create_chat_groq
import prompt
from langchain_groq import ChatGroq

def generate_quiz(topic, difficulty):
    """
    Function to generate quiz answers.
    Returns: response.content (str)
    
    Args:
    - topic (str): Topic of the quiz (e.g., Math, Science)
    - difficulty (str): Difficulty level (e.g., Easy, Medium, Hard)
    """
    prompt_template = prompt.quiz_generator_prompt()

    llm = create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })
    return response.content
