from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.handler import crb_router
from api.validator import Validator
from service import Service
from valute_model import ValutesConfig


@asynccontextmanager
async def lifespan(app: FastAPI):
    service = Service()
    validator = Validator()
    valutes_config = ValutesConfig(valutes=await service.load_data())
    yield {"service": service, "validator": validator, "valutes_config": valutes_config}


app = FastAPI(lifespan=lifespan)

app.include_router(crb_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
