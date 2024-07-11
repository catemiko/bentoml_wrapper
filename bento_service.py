from data import SimpleModelInput, SimpleModelOutput
from init import BentoInit
from service import SimpleRestService

bento_init = BentoInit(SimpleRestService, SimpleModelInput, SimpleModelOutput)

bento_service = bento_init.service()

# bento_service.serve_http()
