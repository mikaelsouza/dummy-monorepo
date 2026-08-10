"""A small, self-contained FastAPI service (distinct from the Titanic model).

Run it locally from the repo root with::

    uvicorn --app-dir projects/web main:app
"""

from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Web Sample Service")


class EchoRequest(BaseModel):
    message: str = Field(..., min_length=1)


@app.get("/")
def root() -> dict:
    return {"service": "web-sample", "endpoints": ["/health", "/echo"]}


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}


@app.post("/echo")
def echo(payload: EchoRequest) -> dict:
    return {"message": payload.message}
