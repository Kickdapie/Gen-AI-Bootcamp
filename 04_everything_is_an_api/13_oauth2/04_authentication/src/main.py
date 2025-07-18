from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from .web.auth import router
from .models.sqlalchemy_models import Base
from .utils.db_dep import engine

app = FastAPI(
    title="OAuth2 Microservice",
    description="A multi-user OAuth2 microservice with login/password signin and Google signin features.",
    version="1.0.0",
    terms_of_service="https://caxgpt.vercel.app/terms/",
    contact={
        "name": "Danny Nguyen",
        "url": "https://localhost:8000/contact/",
        "email": "email@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    servers=[
        {
            "url": "https://localhost:8000",
            "description": "Local server"
        },
    ],
    docs_url="/docs"
)

# SessionMiddleware must be installed to access request.session
<<<<<<< HEAD
app.add_middleware(SessionMiddleware, secret_key="!secret") #allows metadata for request header

app.router.include_router(router, tags=["OAuth2 Authentication"]) #going to use a router

Base.metadata.create_all(bind=engine) #creates sqlalchemy metadata
=======
app.add_middleware(SessionMiddleware, secret_key="!secret")

app.router.include_router(router, tags=["OAuth2 Authentication"])

Base.metadata.create_all(bind=engine)
>>>>>>> sashank/main
