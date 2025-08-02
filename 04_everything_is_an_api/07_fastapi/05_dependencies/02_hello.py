from fastapi import FastAPI, Depends, Query

app : FastAPI = FastAPI()

def dep_check(name:str = Query(None), password:str = Query(None)):
    if not name:
        raise

"""
For this /login endpoint, there are some preliminary checks/actions that 
need to be performed. Specifically, please run dep_check(). 
If dep_check() finishes successfully (i.e., doesn't raise an exception), 
then proceed to run the login() function. If dep_check() raises an HTTPException, 
then immediately stop and return that error to the client.
"""
@app.get("/login", dependencies=[Depends(dep_check)])
def login():
    return True