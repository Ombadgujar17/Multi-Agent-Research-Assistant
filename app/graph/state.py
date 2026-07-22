from typing import TypedDict


class Source(TypedDict):
    title: str
    url: str


class ResearchState(TypedDict):
    query: str

    research: str
    sources: list[Source]

    verified_research: str

    summary: str

    report: str