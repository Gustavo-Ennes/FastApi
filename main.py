"""Fast api main file"""

from fastapi import FastAPI

from app.infrastructure.database import Base, engine
from app.api.routes import address

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(address.router, prefix="/api", tags=["addresses"])
