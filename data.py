from pydantic import Field

from models.data import ModelInputBase, ModelOutputBase


class SimpleModelInput(ModelInputBase):
    number: int = Field(description="Number field for test (input)")


class SimpleModelOutput(ModelOutputBase):
    result: int = Field(description="Number field for test (output)")
