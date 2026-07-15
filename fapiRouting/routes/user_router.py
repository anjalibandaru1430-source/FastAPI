from fastapi import APIRouter

router=APIRouter(prefix='/user',default="User module APIs")

'''
Usage:fetch user details
Rest API URL: http://127.0.0.1:8000/user/
Method Type:GET
Required Fields:None
Access Type:public
'''

@router.get("/")
def get_users():
    return {"msg":"User Module -geting User Details"}


'''
Usage:create new User
Rest API URL: http://127.0.0.1:8000/user/
Method Type:POST
Required Fields:uid,uname,loc
Access Type:public
'''

@router.post("/")
def create_user():
    return {"msg":"New User Created Successfully"}

'''
Usage:update User
Rest API URL: http://127.0.0.1:8000/user/
Method Type:PUT
Required Fields:uid,uname,loc
Access Type:public
'''

@router.put("/")
def create_user():
    return {"msg":" User updated Successfully"}


'''
Usage:delete  User
Rest API URL: http://127.0.0.1:8000/user/
Method Type:DELETE
Required Fields:
Access Type:public
'''
@router.delete("/")
def delete_user():
    return {"msg":"User Deleted succesfully"}