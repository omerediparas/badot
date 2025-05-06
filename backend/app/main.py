import uvicorn
from fastapi import FastAPI, HTTPException
from .db.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.routers.router import api_router
from app.utils import check_postgres_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health_check():
    db_status = check_postgres_connection()

    if db_status is True:
        return {"status_code": 200 , "detail": "ok"}
    else:
        raise HTTPException(
            status_code=500, detail=f"Database connection failed: {db_status}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
