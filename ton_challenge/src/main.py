from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from routes import endpoint
app = FastAPI()



@app.get("/")
def read_root():
    return "this is a url ton a wallet gen :))"

app.include_router(endpoint.router)
