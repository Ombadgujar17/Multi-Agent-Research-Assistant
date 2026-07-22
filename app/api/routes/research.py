from fastapi import APIRouter

from app.graph.workflow import graph
from app.models.request import ResearchRequest
from app.models.response import ResearchResponse

router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):

    result = graph.invoke(
        {
            "query": request.query,
            "research": "",
            "sources": [],
            "verified_research": "",
            "summary": "",
            "report": "",
        }
    )

    return ResearchResponse(
        query=result["query"],
        summary=result["summary"],
        report=result["report"],
        sources=result["sources"],
    )