"""Main application file"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    ''' Welcome message '''
    return "Welcome to Demo Ray"

@app.get("/{random_string}")
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))
