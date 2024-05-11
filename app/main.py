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

        @self.app.get("/")
        async def read_root():
            return {"hello": "this is my first webo"}

        @self.app.get("/items/{item_id}")
        async def read_item(item_id: int, q: Union[str, None] = None):
            return {"item_id": item_id, "q": q}

        # to add a pool to pooles
        @self.app.post("/add_pool/")
        async def add_pool(length: float, width: float, depth: float):
            new_pool = Pool(length, width, depth)
            pooles.append(new_pool)
            return {"message": "Pool added successfully"}

        # get pool details by its code
        @self.app.get("/get_pool/")
        async def get_pool(code: int):
            p = sd.findpoolbyid(code)
            return {f"pool code is {p.code} and the pool depth is {p.depth} its length is {p.length} and the width is {p.width} "}



        @self.app.post("/addbracelet/")
        async def add_brac(request: Request):
            data = await request.json()
            customer_name = data.get("customer_name")
            age = data.get("age")
            code = data.get("code")
            brac = bracelet(customer_name, age, code)
            result = sd.addbracelet(brac)
            print("new customer was added")
            return result

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
    p1 = Pool(2, 2, 5)
    p2 = Pool(3, 2, 5)
    p3 = Pool(2, 2, 5)

    sd.addpool(p1)
    sd.addpool(p2)
    sd.addpool(p3)

    pp1 = proffeional_pool(2, 2, 5, 4)
    pp2 = proffeional_pool(3, 5, 5, 4)
    pp3 = proffeional_pool(7, 5, 7, 8)

    sd.addpool(pp3)
    sd.addpool(pp2)
    sd.addpool(pp1)

    pp1.olympicGamesNames.append("xx1")
    pp1.olympicGamesNames.append("xx2")

    pp2.olympicGamesNames.append("yy2")
    pp2.olympicGamesNames.append("yy3")

    pp3.olympicGamesNames.append("tt1")
    pp3.olympicGamesNames.append("tt2")

    kp1 = kidspool(0.3, 3, 5, 3, True)
    kp2 = kidspool(0.7, 5, 5, 6, False)
    kp3 = kidspool(2, 5, 7, 16, False)

    sd.addpool(kp3)
    sd.addpool(kp2)
    sd.addpool(kp1)

    b1 = bracelet('Oscar Pistorius', 55)
    b2 = bracelet("Svetlana Romashina", 43)
    b3 = bracelet("Katie Ledecky", 25)

    sd.addbracelet(b1)
    sd.addbracelet(b2)
    sd.addbracelet(b3)
    p1.add_customer(b1)
    p1.add_customer(b2)
    b1.add_pool(p1)
    b2.add_pool(p1)

    p2.add_customer(b1)
    p2.add_customer(b3)
    b1.add_pool(p2)
    b3.add_pool(p2)

    p3.add_customer(b1)
    p3.add_customer(b2)
    b1.add_pool(p3)
    b2.add_pool(p3)

    pp1.add_customer(b1)
    pp1.add_customer(b2)
    b1.add_pool(pp1)
    b2.add_pool(pp1)

    pp2.add_customer(b3)
    pp2.add_customer(b2)
    b1.add_pool(pp2)
    b3.add_pool(pp2)

    pp3.add_customer(b1)
    b1.add_pool(pp3)

    kp1.add_customer(b1)
    kp1.add_customer(b1)
    b1.add_pool(kp1)
    b2.add_pool(kp1)

    kp2.add_customer(b2)
    b2.add_pool(kp2)

    kp3.add_customer(b2)
    kp3.add_customer(b1)
    b1.add_pool(kp3)
    b2.add_pool(kp3)

    m1 = Manager("martin", 47, 13000)
    m2 = Manager("alex", 37, 11000)
    m3 = Manager("yaseen", 28, 9000)
    m4 = Manager("taha", 28, 9000)

    sd.addmanager(m1)
    sd.addmanager(m2)
    sd.addmanager(m3)
    sd.addmanager(m4)

    m1.add_pool(p1)
    m1.add_pool(pp1)
    m1.add_pool(kp1)
    m2.add_pool(p2)
    m2.add_pool(pp3)

    p1.manager = m1
    pp1.manager = m1
    kp1.manager = m1
    p2.manager = m2
    pp3.manager = m2

    sd.poolcode_manager_dic[p1.code] = m1
    sd.poolcode_manager_dic[pp1.code] = m1
    sd.poolcode_manager_dic[kp1.code] = m1
    sd.poolcode_manager_dic[p2.code] = m2
    sd.poolcode_manager_dic[pp3.code] = m2

    pooles = []
    instance = fasti()
    instance.run_app()



