from pydantic import BaseModel

class Source(BaseModel):
    title: str
    url: str


class ResearchResponse(BaseModel):
    query: str
    summary: str
    report: str
    sources: list[Source]