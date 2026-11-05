from fastapi import APIRouter

# Get fastapi instance
router = APIRouter()

@router.get('/auth')
async def get_user():
    return {'user': 'authenticated'}