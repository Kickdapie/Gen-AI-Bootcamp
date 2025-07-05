from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(who:str = Body(embed=True)):
<<<<<<< HEAD
    return f"Hello {who}, this uses body/JSON"
=======
    return f"Hello? {who}?"
>>>>>>> sashank/main
