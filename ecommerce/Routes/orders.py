from  fastapi import APIRouter

orders_Router=APIRouter(prefix="/Orders" ,tags= ["orders"]) 

@orders_Router.get('/get')
def get_orders():
    return {"message": "get orders"}
def get_order_by_id(id: int):
    return {"message": f"get order with id {id}"}
def add_order():
    return {"message": "add order"}