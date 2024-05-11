import psycopg2
from app.models.classees import *

db_params = {
    'dbname': 'pools_mall',
    'user': 'postgres',
    'password': '123987zxcoiu',
    'host': 'localhost',
    'port': '5432'
}


class database:
    def __init__(self, db_params, pools_list=None, managers_list=None, code_brac_dic=None, poolcode_manager_dic=None):
        self.pools_list = pools_list if pools_list is not None else []
        self.managers_list = managers_list if managers_list is not None else []
        self.code_brac_dic = code_brac_dic if code_brac_dic is not None else {}
        self.poolcode_manager_dic = poolcode_manager_dic if poolcode_manager_dic is not None else {}
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()

    def addpool(self, pool):
        if pool is None:
            return False
        if pool in self.pools_list:
            return False

        if isinstance(pool, Pool):
            self.pools_list.append(pool)
            return True



    def addbracelet(self, brac):
        try:
            # check if customer code exists
            self.cursor.execute("SELECT code FROM bracelet WHERE code = %s", (brac.code,))
            exist_code = self.cursor.fetchone()

            if exist_code:
                # alredy brac exist
                print(f"braclet with code {brac.code} already exists. You may want to update instead.")

            else:
                # insert it
                self.code_brac_dic[brac.code] = brac
                self.cursor.execute("INSERT INTO bracelet (code, customer_name, age) VALUES (%s, %s, %s)",
                                    (brac.code, brac.customer_name, brac.age))
                self.connection.commit()

        except Exception as e:
            # Handle exceptions
            print(f"Error: {e}")
        finally:
            # Close the cursor in the finally block to ensure it's always closed
            return

    def addmanager(self, manager):
        try:
            # Check if the manager ID already exists
            self.cursor.execute("SELECT id FROM manager WHERE id = %s", (manager.id,))
            existing_id = self.cursor.fetchone()

            if existing_id:
                # Manager with the same ID already exists, handle accordingly (e.g., update)
                print(f"Manager with ID {manager.id} already exists. You may want to update instead.")
            else:
                # Insert the new manager
                self.managers_list.append(manager)
                self.cursor.execute("INSERT INTO manager (id, age, name, salary) VALUES  (%s, %s, %s, %s)",
                                    (manager.id, manager.age, manager.name, manager.salary))
                self.connection.commit()
        except Exception as e:
            # Handle exceptions
            print(f"Error: {e}")
        finally:
            return

    def findpoolbyid(self, poolcode):
        temp = None
        for p in self.pools_list:
            if p.code == poolcode:
                temp = p

        return temp

    def findbracletbyid(self, bracid):
        return self.code_brac_dic.get(bracid)

    def find_manager_byid(self, manid):
        temp = None

        for m in self.managers_list:
            if m.id == manid:
                temp = m

        return temp

    def print_manager_pools(self, m):
        pcode = 0
        i = 0
        toreturn = []
        for key, value in self.poolcode_manager_dic.items():
            if value is m:
                pcode = key
                p = self.findpoolbyid(pcode)
                i += 1
                toreturn.append(p)
                print(f" {i}. {p}")

        if pcode == 0:
            print(f"this manager does not has any pools that he manage")

        return toreturn

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
