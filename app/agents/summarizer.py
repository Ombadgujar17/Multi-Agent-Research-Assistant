from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

summarizer_prompt = Path(
    "app/prompts/summarizer.md"
).read_text(encoding="utf-8")

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

summarizer_agent = create_agent(
    model=llm,
    tools=[]
)

def summarize(verified_research: str) -> str:
    response = summarizer_agent.invoke(
        {
            "messages": [
                SystemMessage(content=summarizer_prompt),
                HumanMessage(content=verified_research)
            ]
        }
    )

    return response["messages"][-1].content


if __name__ == "__main__":
    text = input("Verified Research:\n")
    print(summarize(text))