from abc import ABC, abstractmethod
from typing import Any, Dict, Type

import bentoml

from models.models import ResponseJSON

from .data import ModelInputBase, ModelOutputBase


class RestServiceBase(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def version(self) -> ResponseJSON:
        """
        Prints BentoML version.
        """
        return ResponseJSON(response={"version": bentoml.__version__})

    # TODO Deal with **kwargs cast to ModelInputBase
    @abstractmethod
    def predict(self, **kwargs: Any) -> Type[ModelOutputBase]:
        """
        Base abstract method for predictions API.
        """
        # def predict(self, input: Type[ModelInput]) -> Type[ModelOutput]:
        pass
