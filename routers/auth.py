from fastapi import APIRouter, Depends
from models import Users
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated

# Get fastapi instance
router = APIRouter()

# Pydantic validation for user request
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

# Get db connection for CRUD operation
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/signin')
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email= create_user_request.email,
        username= create_user_request.username,
        first_name= create_user_request.first_name,
        last_name= create_user_request.last_name,
        role= create_user_request.role,
        hashed_password= create_user_request.password,
        is_active=True
    )

    db.add(create_user_model)
    db.commit()
