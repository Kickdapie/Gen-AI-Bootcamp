from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/agent") #get does not work, post prints HTTPie/3.2.4
def get_agent(user_agent:str = Header()):
    print(user_agent)
    return user_agent