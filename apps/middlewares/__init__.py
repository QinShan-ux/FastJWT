from fastapi import FastAPI

from .rate_limit import rate_limit_middleware
from .timing import timing_middleware


def register_custom_middleware(app: FastAPI):
    app.middleware("http")(rate_limit_middleware)
    app.middleware("https")(timing_middleware)
