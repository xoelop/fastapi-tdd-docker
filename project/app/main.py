# project/app/main.py

import logging
import os

from fastapi import Depends, FastAPI

log = logging.getLogger("uvicorn")

from app.api import ping, summaries
from app.config import Settings, get_settings
from app.db import init_db


def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
