   

from model import create_chat_groq
import prompt
from langchain_groq import ChatGroq

def generate_poem(topic):
     """
     Function to generate poem
     Returns : response.content(str)

     Args : topic ( str) - topic of the poem

     """
     prompt_template = prompt.poem_generator_prompt()

     llm=create_chat_groq()

     chain = prompt_template | llm

     response = chain.invoke({
          "topic" : topic
          })
     return response.content