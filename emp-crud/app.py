from fastapi import FastAPI
from routes.emp_router import router as emp_router
app=FastAPI()

'''
usage:Application root request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Request Fields:None 
Access Type:Public
'''
@app.get('/')
def root_request():
    return {'msg':'Application Root Requst'}


app.include_router(emp_router)