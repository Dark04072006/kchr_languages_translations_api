import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends as FastAPIDepends, HTTPException

from dishka.integrations.fastapi import inject, Depends as DishkaDepends

from app.database.translation_dao import TranslationDAO
from app.models.translation import Translation
from app.web.schemas import PaginationParams, TranslationParams


router = APIRouter(prefix="/translations", tags=["Словарь"])


@router.get("/", response_model=list[Translation])
@inject
async def get_translations(
    translation_dao: Annotated[TranslationDAO, DishkaDepends()],
    pagination_params: Annotated[PaginationParams, FastAPIDepends()],
    translation_params: Annotated[TranslationParams, FastAPIDepends()],
) -> list[Translation]:
    try:
        pagination_params.validate_params()

    except ValueError as e:
        raise HTTPException(400, detail=str(e))

    else:
        return await asyncio.to_thread(
            translation_dao.get_like,
            translation_params.variation,
            translation_params.word,
            pagination_params.limit,
            pagination_params.offset,
        )
