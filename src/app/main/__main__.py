import uvicorn
from fastapi import FastAPI

from dishka.integrations.fastapi import DishkaApp

from app.web.routes import router
from app.main.ioc import DbAdaptersProvider


def create_app() -> DishkaApp:
    fastapi_app = FastAPI()
    fastapi_app.include_router(router)

    return DishkaApp(providers=[DbAdaptersProvider()], app=fastapi_app)


if __name__ == "__main__":
    uvicorn.run(create_app())
