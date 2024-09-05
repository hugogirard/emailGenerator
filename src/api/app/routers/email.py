from fastapi import APIRouter

router = APIRouter(
    prefix="/api/email",
    tags=["email"],
)

@router.get("/generate")
async def generate_email():
    return {"message": "Email generated successfully"}