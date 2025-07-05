from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{who}")
def greet(who:str):
<<<<<<< HEAD
    return f"Hello there, {who}?"

'''
This is a route with a path parameter.
 /hi is a fixed part of the URL path
It must be in the URL exactly as written.

 {who} is a variable part (a path parameter)
It can be anything the user types after /hi/.

Example:
http://localhost:8000/hi/john
'''
=======
    return f"Hello? {who}?"
>>>>>>> sashank/main

# @app.get("/hi/{who}/piaic")
# def greet(who:str):
#     return f"Hello? {who}?"