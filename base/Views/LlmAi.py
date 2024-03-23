# chatapp/views.py

from django.http import JsonResponse
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

def chat(request):
    api_key = os.getenv("OPENAI")
    print(api_key)
    llm = ChatOpenAI(api_key=api_key)
    text_data = request.POST.get('text')
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are a helpful AI providing explanations of reports based on previous conversations with the user. If there is any data within UserReport('''Anything'''), please train yourself with it."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(text_data)
        ]
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory
    )
    
    response = conversation.generate_response()
    
    return JsonResponse({"response": response})
