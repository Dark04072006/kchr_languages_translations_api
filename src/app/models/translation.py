from dataclasses import dataclass

from app.models.variation import TranslationVariation


@dataclass
class Translation:
    id: int
    word: str
    translation: str
    variation: TranslationVariation
