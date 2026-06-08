from fastapi import FastAPI
from routes.userRouter import user_router
app=FastAPI()
app.include_router(user_router)
'''
usage : application root request
rest api url : http://127.0.0.1:8000/
method :GET
required fields ; none 
Access type : none
'''
@app.get("/")
def index_page():
    return{"msg": "Application index page"}

