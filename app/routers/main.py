from fastapi import FastAPI, Request
from typing import Union
import uvicorn
from app.models import systemdatabase  # Import your database model
from app.models.classees import *      # Import your classes as needed

# Initialize the FastAPI instance at the module level
app = FastAPI()

# Set up your database connection parameters
db_params = {
    'dbname': 'pools_mall',
    'user': 'postgres',
    'password': '123987zxcoiu',
    'host': 'db',
    'port': '5432'
}

# 'host': 'localhost', when dealing with loal postgresql database
sd = systemdatabase.database(db_params)

# Define your routes
@app.post("/add_pool/")
async def add_pool(length: float, width: float, depth: float, managerid: int):
    new_pool = Pool(length, width, depth, managerid)
    sd.addpool(new_pool)
    return {"message": "Pool added successfully"}

@app.get("/get_pool/")
async def get_pool(poolcode: int):
    try:
        p = sd.findpoolbyid(poolcode)
        if p is None:
            return {"error": f"No pool found with code {poolcode}"}
        return {
            f"pool code is {p.code}, pool depth is {p.depth}, its length is {p.length}, and the width is {p.width}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

@app.post("/addbracelet/")
async def add_brac(code: int, customer_name: str, age: int):
    brac = bracelet(code, customer_name, age)
    result = sd.addbracelet(brac)
    return result

@app.post("/addmanager/")
async def add_manager(id: int, name: str, age: int, salary: int):
    manager = Manager(id=id, name=name, age=age, salary=salary)
    response = sd.addmanager(manager)
    return response

# Running the app directly using Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
