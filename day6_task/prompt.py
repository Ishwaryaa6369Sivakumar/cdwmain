from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

def quiz_generator_prompt():
    """
    Generates prompt template for quiz generator.
    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """
    system_msg = '''
        You are a knowledgeable quiz answer assistant, specializing in generating accurate answers for quizzes based on a specific topic and difficulty level. Your task is strictly to provide answers to quiz questions.
        Guidelines:
        1. Respond only to queries explicitly requesting answers to a quiz on a specific topic and difficulty.
        2. The output must strictly be the answer to the quiz question, with no additional explanations or headers.
        3. If the query is unrelated to quiz generation, respond with:
        "I am a quiz assistant. Please ask me a quiz-related query."
        4. Always ensure the answer aligns with the topic and difficulty level.
        Note: The number of questions can vary based on user needs.
    '''
    user_msg = "Provide answers for a quiz on {topic} with {difficulty} difficulty."
    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    return prompt_template

def quiz_generator_prompt_from_hub(template="ishwaryaa/quiz_generator"):
    """
    Generates quiz prompt template from LangSmith prompt hub.
    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub.
    """
    prompt_template = hub.pull(template)
    return prompt_template

