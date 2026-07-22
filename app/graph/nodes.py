from app.graph.state import ResearchState

from app.agents.researcher import research
from app.agents.fact_checker import fact_check
from app.agents.summarizer import summarize
from app.agents.report_generator import generate_report


def research_node(state: ResearchState):

    result = research(state["query"])

    return {
        "research": result["research"],
        "sources": result["sources"],
    }


def fact_checker_node(state: ResearchState):

    return {
        "verified_research": fact_check(
            state["research"]
        )
    }


def summarizer_node(state: ResearchState):

    return {
        "summary": summarize(
            state["verified_research"]
        )
    }


def report_generator_node(state: ResearchState):

    return {
        "report": generate_report(
            summary=state["summary"],
            sources=state["sources"]
        )
    }