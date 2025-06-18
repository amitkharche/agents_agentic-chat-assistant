from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain.memory import ConversationBufferMemory
import os
from src.tools import tools

# ✅ Load OpenAI Chat model
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo"
)

# ✅ Conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ✅ Initialize the agent
agent_executor: AgentExecutor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True  # ✅ Allows retry on malformed output
)

# ✅ Response function
def get_agentic_response(user_input: str) -> str:
    return agent_executor.run(user_input)
