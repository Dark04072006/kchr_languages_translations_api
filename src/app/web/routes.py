from json import dumps
from typing import Annotated
from dataclasses import asdict

from flask import Blueprint, Request, Response, jsonify

from dishka.integrations.flask import inject, Depends

from app.models.translation import Translation
from app.models.variation import TranslationVariation
from app.database.translation_dao import TranslationDAO
from app.web.schemas import PaginationParams, TranslationParams


blueprint = Blueprint("translations", __name__, url_prefix="/translations")


@blueprint.get("/")
@inject
def get_translations(
    request: Annotated[Request, Depends()],
    translation_dao: Annotated[TranslationDAO, Depends()],
) -> list[Translation] | tuple[Response, int]:
    pagination_params = PaginationParams(
        request.args.get("limit", 20, int),
        request.args.get("offset", 0, int),
    )
    translation_params = TranslationParams(
        request.args.get("word", "", str),
        request.args.get(
            "variation",
            TranslationVariation.RUSSIAN_CIRCASSIAN.value,
            str,
        ),
    )
    try:
        pagination_params.validate_params()
    except ValueError as e:
        return jsonify({"detail": str(e)}), 400

    else:
        translations = translation_dao.get_like(
            translation_params.variation,
            translation_params.word,
            pagination_params.limit,
            pagination_params.offset,
        )
        return [
            dumps(asdict(translation), ensure_ascii=False)
            for translation in translations
        ]
