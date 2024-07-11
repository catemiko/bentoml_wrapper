from typing import Any, Dict

from pydantic import BaseModel

from data import SimpleModelInput, SimpleModelOutput
from models.models import ResponseJSON
from models.service import RestServiceBase


class SimpleRestService(RestServiceBase):
    def __init__(self) -> None:
        pass

    def version(self) -> ResponseJSON:
        return super().version()

    def predict(self, **kwargs: Any) -> SimpleModelOutput:
        # def predict(self, input: ModelInput) -> ModelOutput:
        input = SimpleModelInput(**kwargs)
        response = SimpleModelOutput(
            response={"result": f"{input.text}_kek"}, result=input.number + 1337
        )
        return response
