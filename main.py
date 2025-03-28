from fastapi import FastAPI


from src.routers import contacts_routes


app = FastAPI()

app.include_router(contacts_routes.router, prefix="/api")


@app.get("/")
async def read_root():
    return {"Welcome to FastAPI"}
