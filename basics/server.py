from fastapi import FastAPI

app=FastAPI()

""" 
Usage: Application Root Request
RestAPI URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Access Type:public """

@app.get("/")
def root_request():
    return {"msg":True}

'''
Usage: get all Products
RestAPI URL: http://127.0.0.1:8000/products/read
Method Type:GET
Required Fields: None 
Access Type:public
'''
@app.get("/products/read")
def get_products():
    return {"smg":"Getting all products"}


""" 
Usage: update product by id
RestAPI URL: http://127.0.0.1:8000/products/update/101
Method Type:PUT
Required Fields: pid,pname,price,category 
Access Type:public """


@app.put("/products/update")
def update_product():
    return {"msg":"Product updated successfully"}