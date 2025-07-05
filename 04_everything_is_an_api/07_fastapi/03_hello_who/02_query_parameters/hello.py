from fastapi import FastAPI

app = FastAPI()

# @app.get("/hi")
# def greet(who:str):
#     return f"Hello? {who}?"

@app.get("/hi") 
def greet(who):
<<<<<<< HEAD
    return f"Hello mister {who}?"
=======
    return f"Hello? {who}?"
>>>>>>> sashank/main
