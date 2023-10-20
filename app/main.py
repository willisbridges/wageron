from fastapi import FastAPI

app = FastAPI()

# include routers
# app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(bets.router, prefix="/bets", tags=["users"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    # run app with uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
