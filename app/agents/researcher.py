from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain.agents import create_agent
from app.tools import tavily_search
from pathlib import Path
import json
from langchain_core.messages import ToolMessage

researcher = Path("app/prompts/researcher.md").read_text()

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

research_agent = create_agent(
    model=llm,
    tools=[tavily_search.search_tool]
)

def research(query: str):

    response = research_agent.invoke(
        {
            "messages": [
                SystemMessage(content=researcher),
                HumanMessage(content=query)
            ]
        }
    )

    messages = response["messages"]

    research_text = messages[-1].content

    sources = []

    for message in messages:

        if isinstance(message, ToolMessage):

            tool_data = json.loads(message.content)

            for result in tool_data.get("results", []):

                sources.append(
                    {
                        "title": result["title"],
                        "url": result["url"],
                    }
                )

    return {
        "research": research_text,
        "sources": sources,
    }


if __name__ == "__main__":
    query = input("Research Topic: ")
    print(research(query))

