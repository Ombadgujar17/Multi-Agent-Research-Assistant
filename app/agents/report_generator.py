from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

report_generator_prompt = Path(
    "app/prompts/report_generator.md"
).read_text(encoding="utf-8")

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

report_generator_agent = create_agent(
    model=llm,
    tools=[]
)

def generate_report(summary: str, sources: list[dict]) -> str:
    references = "\n".join(
        f"- {source['title']}\n  {source['url']}"
        for source in sources
        )
    response = report_generator_agent.invoke(
        {
            "messages": [
                SystemMessage(content=report_generator_prompt),
                HumanMessage(content=f"""
                Summary:{summary}
                References:{references}
                Generate a professional research report.
                Use ONLY the references provided above.
                Do not invent or fabricate references.
                """
)
            ]
        }
    )

    return response["messages"][-1].content


if __name__ == "__main__":
    text = input("Summary:\n")
    print(generate_report(text))