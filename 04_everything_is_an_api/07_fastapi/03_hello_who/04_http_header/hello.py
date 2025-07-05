from fastapi import FastAPI, Header

app = FastAPI()

<<<<<<< HEAD
@app.get("/hi") #use the get command not post
=======
@app.post("/hi")
>>>>>>> sashank/main
def greet(who:str = Header()):
    return f"Hello? {who}?"