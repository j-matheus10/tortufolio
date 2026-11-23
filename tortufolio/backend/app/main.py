from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.routers.auth import router as auth_router

from app.core.database import get_db

app = FastAPI(
    title="TortuFolio API",
    description="API de gestión documental para la DIT — UAH",
    version="0.1.0",
)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"status": "ok", "app": "TortuFolio"}


@app.get("/health/db")
async def health_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    result.scalar()
    return {"db": "connected"}
