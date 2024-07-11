from abc import ABC, abstractmethod
from typing import Any, Type

from .data import ModelInputBase, ModelOutputBase


class RestServiceBase(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    # TODO Deal with **kwargs cast to ModelInputBase
    @abstractmethod
    def predict(self, **kwargs: Any) -> Type[ModelOutputBase]:
        # def predict(self, input: Type[ModelInput]) -> Type[ModelOutput]:
        pass
