from typing import List

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def create_summary(payload: SummaryPayloadSchema) -> TextSummary:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary


async def get_summary(id: int) -> TextSummary:
    summary = await TextSummary.filter(id=id).first()
    if summary:
        return summary
    return None


async def get_summaries() -> List[TextSummary]:
    summaries = await TextSummary.all()
    return summaries
