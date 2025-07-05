from fastapi import FastAPI

<<<<<<< HEAD
app : FastAPI = FastAPI()  #This line creates an instance of the FastAPI application.

@app.get("/")              #This is a route decorator. “When someone makes a GET request to the / path (homepage), run the function below.”
def index() -> str:                #-> str is a return type annotation, saying this function returns a string.
    return "I am Danny Nguyen , 123 , abc"       #When someone visits your API's root path (/), they'll see this exact string as a response in their browser or API client like Postman or curl.
=======
app : FastAPI = FastAPI()

@app.get("/")
def index() -> str:
    return "Pakistan zinda bad , 123 , abc"
>>>>>>> sashank/main
