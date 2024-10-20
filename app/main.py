import app.models.systemdatabase
from app.models.systemdatabase import *
from fastapi import FastAPI, Request
from typing import Union
import uvicorn

from app.models.classees import *



class fasti:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()

    def setup_routes(self):



        # to add a pool to pooles
        @self.app.post("/add_pool/")
        async def add_pool(length: float, width: float, depth: float, managerid: int):
            new_pool = Pool(length, width, depth, managerid)
            sd.addpool(new_pool)
            return {"message": "Pool added successfully"}

        # get pool details by its code
        @self.app.get("/get_pool/")
        async def get_pool(poolcode: int):
            try:
                # Call your function to find the pool by id (code)
                p = sd.findpoolbyid(poolcode)
                # Check if the pool was found
                if p is None:
                    return {"error": f"No pool found with code {poolcode}"}
                # Return pool details if found
                return {
                    f"pool code is {p.code}, pool depth is {p.depth}, its length is {p.length}, and the width is {p.width}"}
            except Exception as e:
                return {"error": f"An error occurred: {str(e)}"}

        @self.app.post("/addbracelet/")
        async def add_brac(code:int, customer_name: str, age: int ):
            brac = bracelet(code,customer_name, age)
            result = sd.addbracelet(brac)
            return result


        @self.app.post("/addmanager/")
        async def add_manager(id: int, name: str, age: int, salary: int):
            manager = Manager(id=id, name=name, age=age, salary=salary)
            response = sd.addmanager(manager)
            return response






    # sd.close_connection()
    def run_app(self):
        uvicorn.run(self.app, host="127.0.0.1", port=8001)


if __name__ == '__main__':

    db_params = {
        'dbname': 'pools_mall',
        'user': 'postgres',
        'password': '123987zxcoiu',
        'host': 'localhost',
        'port': '5432'
    }

    # sd = app.models.systemdatabase.database(db_params)
    sd = database(db_params)































    instance = fasti()
    instance.run_app()



