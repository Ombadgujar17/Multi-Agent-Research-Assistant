from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage

fact_checker_prompt = Path("app/prompts/fact_checker.md").read_text()

load_dotenv()

llm = ChatGroq(
    model="Qwen/Qwen3.8-27B"
)

fact_check_agent = create_agent(
    model=llm,
    tools=[]
    )

def fact_check(research_output: str) -> str:
    response = fact_check_agent.invoke(
        {
            "messages": [
                SystemMessage(content=fact_checker_prompt),
                HumanMessage(content=research_output)
            ]
        }
    )

    return response["messages"][-1].content


if __name__ == "__main__":
    research_output = input("Enter the research output to fact-check: ")
    print(fact_check(research_output))