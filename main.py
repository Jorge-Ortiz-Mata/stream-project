from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(streaming=True)

prompt = ChatPromptTemplate.from_messages([
  ("human", "{content}")
])

chain = LLMChain(llm=chat, prompt=prompt)

chain("Dime una broma")

print(chain)



# messages = prompt.format_messages(content="Dime un poema de 4 lineas")

# for message in chat.stream(messages):
#   print(message.content)
