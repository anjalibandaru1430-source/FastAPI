from fastapi import APIRouter

user_router=APIRouter(prefix="/users",tags=["users"])

@user_router.get("/")
def get_user():
    return {"msg":"get user details"}
@user_router.post("/")
def create_user():
    return {"msg":"create user details"}
@user_router.put("/")
def update_user():
    return {"msg":"update user details"}
@user_router.delete("/")
def delete_user():
    return {"msg":"delete user details"}