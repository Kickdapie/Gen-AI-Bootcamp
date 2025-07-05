# Example 01 old way with helper function
# from fastapi import FastAPI, Depends, Query

# app : FastAPI = FastAPI()

# def login(username : str , password : str ):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Successful"}
#     else:
#         return {"message" : "Login Failed"}
    

# @app.get("/login")
# def login_api(user,password):
#     result = login(user,password) # custom calling
#     return result
# Example 02 new way with Dependencies injection
from fastapi import FastAPI, Depends, Query
from typing import Annotated

app : FastAPI = FastAPI()

# depency function
def dep_login(username : str = Query(None), password : str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message" : "Login Successful"}
    else:
        return {"message" : "Login Failed"}
    
@app.get("/signin")
def login_api(user :  Annotated[dict,Depends(dep_login)]):
<<<<<<< HEAD
    return user


"""
When someone sends a GET request to /signin with username and password as query parameters, this happens:

FastAPI sees that login_api has a dependency on dep_login.

It calls dep_login automatically, passing in the username and password from the query string.

The return value of dep_login is passed as the user argument in login_api.

login_api simply returns the result.
"""
=======
    return user
>>>>>>> sashank/main
