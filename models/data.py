from typing import Any, Dict

from _bentoml_sdk.io_models import IODescriptor
from pydantic import BaseModel, Field


class ModelInputBase(IODescriptor, BaseModel):
    """
    Base input data model for API.
    """

    text: str = Field(description="Simple text field for test")


class ModelOutputBase(IODescriptor, BaseModel):
    """
    Base output data model for API.
    """

    response: Dict[str, Any] = Field(description="Output JSON dict")
