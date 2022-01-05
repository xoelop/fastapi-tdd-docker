from typing import List, Optional, Union

from fastapi import APIRouter, HTTPException, status

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post(
    "/", response_model=SummaryResponseSchema, status_code=status.HTTP_201_CREATED
)
async def create_summary(payload: SummaryPayloadSchema) -> SummarySchema:
    response = await crud.create_summary(payload)
    return response


@router.get("/{id}", response_model=SummarySchema)
async def get_summary(id: int) -> SummarySchema:
    summary = await crud.get_summary(id)
    if not summary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Summary not found"
        )
    return summary


@router.get("/", response_model=List[SummarySchema])
async def get_summaries() -> List[SummarySchema]:
    summaries = await crud.get_summaries()
    return summaries
