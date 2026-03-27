from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

from app.core.limiter import limiter
from app.api.contact import router as contact_router

from app.db.base import Base
from app.db.session import engine

import logging

app = FastAPI(title="Contact Form API")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# create tables
Base.metadata.create_all(bind=engine)

# Rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(contact_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "API is running"}
