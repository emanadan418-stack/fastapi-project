from fastapi import FastAPI
#from .database import engine
#from . import models, oauth2
from .posts import router as posts_router
from .users import router as users_router
from .auth import router as auth_router
from .vote import router as vote_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#models.Base.metadata.create_all(bind=engine)
app.include_router(posts_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(vote_router)

@app.get("/")
def root():
    return {"message": "Hello Adan"}
