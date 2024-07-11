from typing import Type

from _bentoml_sdk.method import APIMethod
from _bentoml_sdk.service import Service, service

from models.data import ModelInputBase, ModelOutputBase
from models.service import RestServiceBase


class BentoInit:
    _bento_service: Service[RestServiceBase]

    def __init__(
        self,
        service_cls: Type[RestServiceBase],
        input_cls: Type[ModelInputBase],
        output_cls: Type[ModelOutputBase],
    ) -> None:
        self._bento_service = service(service_cls)

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
        return self._bento_service
