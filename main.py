
from fastapi import FastAPI

# Import API routers
from economy_api.economy_router import router as economy_router
from wicket_api.wicket_router import router as wicket_router
from entropy_api.entropy_router import router as entropy_router

# Initialize FastAPI application
app = FastAPI(
    title="Cricket Bowling Intelligence APIs",
    description="Advanced cricket analytics using statistical intelligence models",
    version="1.0.0"
)

# Register Routers
app.include_router(economy_router)
app.include_router(wicket_router)
app.include_router(entropy_router)


@app.get("/")
async def root():
    """
    Root health endpoint.
    """

    return {
        "status": "healthy",
        "message": "Cricket Bowling Intelligence APIs are running",
        "available_apis": [
            "Economy Deviation API",
            "Wicket Probability API",
            "Control Entropy API"
        ]
    }
