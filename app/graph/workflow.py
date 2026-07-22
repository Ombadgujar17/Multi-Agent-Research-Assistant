from langgraph.graph import StateGraph, START, END

from app.graph.state import ResearchState
from app.graph.nodes import (
    research_node,
    fact_checker_node,
    summarizer_node,
    report_generator_node,
)

builder = StateGraph(ResearchState)

builder.add_node("research", research_node)
builder.add_node("fact_check", fact_checker_node)
builder.add_node("summarize", summarizer_node)
builder.add_node("report", report_generator_node)

builder.add_edge(START, "research")
builder.add_edge("research", "fact_check")
builder.add_edge("fact_check", "summarize")
builder.add_edge("summarize", "report")
builder.add_edge("report", END)

graph = builder.compile()