from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi") #use the get command not post
def greet(who:str = Header()):
    return f"Hello? {who}?"