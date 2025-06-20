from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/hi") 
def greet():
    return "Hello World!!!!"

@app.get("/hi/{variable}")
def greet_with_name(variable: str):
    return "Hello? World, " + variable

# print(__name__)

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("hello1:app", reload=True)