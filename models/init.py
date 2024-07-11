from typing import Type

from _bentoml_sdk.io_models import IODescriptor
from _bentoml_sdk.method import APIMethod
from _bentoml_sdk.service import Service, service

from models.data import ModelInputBase, ModelOutputBase
from models.models import InputNone, ResponseJSON
from models.service import RestServiceBase


class BentoInit:
    """
    Wrapper class for BentoML service.
    """

    _bento_service: Service[RestServiceBase]

    def __init__(
        self,
        service_cls: Type[RestServiceBase],
        input_cls: Type[ModelInputBase],
        output_cls: Type[ModelOutputBase],
    ) -> None:
        """
        Initializes BentoML service with given REST service class, input/output data model classes.
        """
        self._bento_service = service(service_cls)

        self._bento_service.apis.update(
            {
                "version": APIMethod(
                    service_cls.version,
                    route="/version",
                    name="version",
                    input_spec=InputNone,
                    output_spec=ResponseJSON,
                )
            }
        )

        self._bento_service.apis.update(
            {
                "predict": APIMethod(
                    service_cls.predict,
                    route="/predict",
                    name="predict",
                    input_spec=input_cls,
                    output_spec=output_cls,
                )
            }
        )

    def service(self) -> Service:
        """
        Returns Bento service.
        """
        return self._bento_service
