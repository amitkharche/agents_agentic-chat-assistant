from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
import os
from tools import tools

# Initialize LLM
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo")

# Memory for tracking conversation
memory = ConversationBufferMemory(memory_key="chat_history")

# Create agent with tool usage
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

def get_agentic_response(user_input):
    return agent.run(user_input)
