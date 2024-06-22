from sqlmodel import SQLModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
import httpx

from database.db_connection import engine, get_session
from database.models import HQProduct, LocalProduct

from routers.local_products import local_products_router
from routers.hq_products import hq_products_router
from routers.authentication import authentication_router
from routers.products_joined import products_joined_router

origins = ['http://localhost:5173', 'http://localhost', 'localhost:5000']
HQ_API_URL = "http://localhost:7000"

SQLModel.metadata.create_all(engine)

# Create a FastAPI instance
app = FastAPI()

scheduler = AsyncIOScheduler()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers for controllers
app.include_router(hq_products_router, tags=["HQ Products"])
app.include_router(local_products_router, tags=["Local Products"])
app.include_router(products_joined_router, tags=["Products Joined"])
app.include_router(authentication_router, tags=["Authentication"])


async def fetch_and_save_hq_products():
    from mock import mocked_hq_products
    from requests.exceptions import RequestException

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(HQ_API_URL)
            response.raise_for_status()
            products_data = response.json()
    except (httpx.HTTPStatusError, httpx.ConnectError) as e:
        # Handle HTTP request errors or HTTP status errors
        print(f"Error fetching HQ products: {e}")
        # Return mocked data instead
        products_data = mocked_hq_products
    try:
        with get_session() as session:
            session.execute(HQProduct.__table__.delete())  # Clear existing data
            for product_data in products_data:
                product = HQProduct(**product_data)
                if session.get(LocalProduct, product.id) is None:
                    local_product = LocalProduct(hq_product_id=product.id, amount_in_stock=0)
                    session.add(local_product)
                session.add(product)
            session.commit()
        print("HQ products fetched and saved")
    except Exception as e:
        print(f"Error saving HQ products: {e}")


@app.on_event("startup")
def startup_event():  # Schedule the initial sync
    scheduler.add_job(
        fetch_and_save_hq_products,
        trigger=IntervalTrigger(minutes=30),
        id="fetch_hq_products",
        replace_existing=True
    )
    scheduler.start()


@app.on_event("shutdown")
def shutdown_event():  # Shutdown the scheduler
    scheduler.shutdown()


@app.get("/")
def read_root():
    return {"Hello": "Clothex Summer API"}


if __name__ == "__main__":
    # Create db and tables
    from database.db_connection import create_db_and_tables
    create_db_and_tables()

    # Run the application using uvicorn
    from uvicorn import run
    run(app, host='0.0.0.0', port=8000)
