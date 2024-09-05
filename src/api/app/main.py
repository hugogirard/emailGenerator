from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from .routers import email_router

app = FastAPI()

app.include_router(email_router)

# Redirect to the API documentation
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")