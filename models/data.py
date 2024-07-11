from typing import Any, Dict

from _bentoml_sdk.io_models import IODescriptor
from pydantic import BaseModel, Field


class ModelInputBase(IODescriptor, BaseModel):
    text: str = Field(description="Simple text field for test")


class ModelOutputBase(IODescriptor, BaseModel):
    response: Dict[str, Any] = Field(description="Output JSON dict")
