from fastapi import APIRouter
router=APIRouter(prefix="/products")

products=[
    {'pid':101,'pname':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'pname':'Lenovo Mouse','price':300,'category':'Electronics'},
    {'pid':103,'pname':'Color Pen','price':10,'category':'Stationary'},
    {'pid':104,'pname':'Think Pad','price':800000,'category':'Electronics'},
    {'pid':105,'pname':'Mobile Phone','price':25000,'category':'Electronics'},
    {'pid':106,'pname':'Mobile Cover','price':250,'category':'Electronics'}
]

'''
Usage:fetch all products
RestAPI URL: http://127.0.0.1:8000/products/
Method Type: GET
Required Fields:None
Access Type:Public
'''
@router.get("/")
def get_products():
    return products 



'''
Usage:fetch product by id
RestAPI URL: http://127.0.0.1:8000/products/stationary/101
Method Type: GET
Required Fields:None
Access Type:Public
'''

@router.get("/{prod_id}")
def get_product_details(prod_id: int):
    for product in products:
        if product["pid"] == prod_id:
            return product
    return {"message": "Product not found"}


""" 
@router.get("/{prod_id}")
def get_product_details(prod_id:int):
    product=tuple(filter(lambda p:p['pid']==prod_id,products))
    return product
"""

""" @router.get("/{category}/{pid}")
def get_product_details(category:str,pid:int):
    print(category)
    print(pid)
    return {} """