from fastapi import FastAPI

from routes.user_router import router as user_router
from routes.product_router import rotuter as product_router
app=FastAPI()

'''
Usage:Application Root
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:public
'''
@app.get("/")
def root_request():
    return {"message":"Applicaton Root Request"}

app.include_router(user_router)
app.include_router(product_router)
