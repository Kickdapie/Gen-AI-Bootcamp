from fastapi import FastAPI, Header

app = FastAPI()

<<<<<<< HEAD
@app.post("/agent") #get does not work, post prints HTTPie/3.2.4
=======
@app.post("/agent")
>>>>>>> sashank/main
def get_agent(user_agent:str = Header()):
    print(user_agent)
    return user_agent