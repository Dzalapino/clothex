from fastapi import FastAPI
from sqlmodel import SQLModel
from database.db_connection import engine
from routers.local_products import local_products_router
from routers.authentication import authentication_router
from fastapi.middleware.cors import CORSMiddleware

origins = ['http://localhost:5173', 'http://localhost', 'localhost:5000']

SQLModel.metadata.create_all(engine)

# Create a FastAPI instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers for controllers
app.include_router(local_products_router, tags=["Local Products"])
app.include_router(authentication_router, tags=["Authentication"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # Run the application using uvicorn
    from uvicorn import run
    run(app, host='0.0.0.0', port=8000)
