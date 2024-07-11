from typing import Any

from data import SimpleModelInput, SimpleModelOutput
from models.service import RestServiceBase

class SimpleRestService(RestServiceBase):
    def __init__(self) -> None:
        pass

    def predict(self, **kwargs: Any) -> SimpleModelOutput:
    # def predict(self, input: ModelInput) -> ModelOutput:
        input = SimpleModelInput(**kwargs)
        response = SimpleModelOutput(
            response={"result": f"{input.text}_kek"}, result=input.number + 1337
        )
        return response
