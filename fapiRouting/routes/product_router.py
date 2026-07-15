from fastapi import APIRouter

rotuter=APIRouter(prefix="/products")


@rotuter.get("/read")
def get_products():
    return {"msg":"Gettin all products"}

@rotuter.post("/create")
def create_product():
    return {"msg":"Product Created Successfully"}

@rotuter.put("/update")
def update_product():
    return {"msg":"Product Updated succesfully"}

@rotuter.delete("/del")
def delete_product():
    return {"msg":"Deleting all products"}