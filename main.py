from dotenv import load_dotenv
from pydantic import BaseModel
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# #llm = ChatOpenAI(model="gpt-4")
# llm = ChatAnthropic(model="claude-3-5-sonnet-202410022")
# response = llm.invoke("What is the meaning of life?")
# print(response)

from google import genai

class ResearchResponse(BaseModel):
    topic:str
    summary:str
    Sources:list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistent that will help generate a research paper.
            Answer the user query and use neccessary tools.
            Wrap the output in the format and provide no other text\n{format_instructions}
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder","{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"query": "what is the capital of France?"})
print(raw_response)
