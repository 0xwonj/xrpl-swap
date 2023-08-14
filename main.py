from uvicorn import run

from app.common.config import settings


if __name__ == "__main__":
    run("app.main:app", host="127.0.0.1", port=8000, reload=settings.LIVE_RELOAD)
