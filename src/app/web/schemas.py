from dataclasses import dataclass

from app.models.variation import TranslationVariation


@dataclass
class TranslationParams:
    word: str
    variation: TranslationVariation


@dataclass
class PaginationParams:
    limit: int = 20
    offset: int = 0

    def validate_params(self) -> None:
        if abs(self.offset - self.limit) > 20:
            raise ValueError(
                "The difference between offset and limit cannot be greater than 20."
            )
