from typing import Any, Dict

from _bentoml_sdk.io_models import IODescriptor
from pydantic import BaseModel, Field


class ResponseJSON(IODescriptor, BaseModel):
    """
    Wrapper of BaseModel for JSON response.
    """

    response: Dict[str, Any] = Field(description="Any JSON document")


class InputNone(IODescriptor, BaseModel):
    """
    Wrapper of BaseModel for none input.
    """

    pass


# TODO Not used now
class OutputNone(IODescriptor, BaseModel):
    """
    Wrapper of BaseModel for none output.
    """

    pass
