from fastapi import FastAPI
import models
from database import engine
from routers import todos, auth
from fastapi.middleware.cors import CORSMiddleware

# Get fastapi instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# creates the required table in db based on models file configuration
models.Base.metadata.create_all(bind = engine)

app.include_router(todos.router)
app.include_router(auth.router)

#comment by Anshul