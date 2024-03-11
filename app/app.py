from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(
    title="NoPaper",
    description="NoPaper API",
    version="0.1.0",
    root_path="/api/v1",
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


from app import auth, docs
app.include_router(docs.router)
app.include_router(auth.router)
