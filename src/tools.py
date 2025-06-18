from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper

# Wikipedia Search Tool
wikipedia = WikipediaAPIWrapper()

wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=wikipedia.run,
    description="Useful for answering general knowledge questions by searching Wikipedia."
)

tools = [wikipedia_tool]
