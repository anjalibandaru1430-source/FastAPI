from fastapi import FastAPI
app=FastAPI()
@app.post("/createuser")
def createuser():
    return{"message":"user created succesfully"}
@app.get("/readuser")
def readuser():
    return{"message":"user read succesfully"}
@app.put("/updateuser")
def updateuser():
    return{"message":"user updated succesfully"}
@app.delete("/deleteuser")
def deleteuser():
    return{"message":"user deleted succesfully"}




    #>uvicorn app:app --reload