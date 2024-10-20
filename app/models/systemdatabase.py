import psycopg2
from app.models.classees import *




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
        try:
            self.cursor.execute("SELECT code FROM  pool WHERE code = %s", (pool.code,))
            does_exist= self.cursor.fetchone()

            if does_exist:
                print(f"this pool with code {pool.code} is alredy exist")

            else:self.cursor.execute("INSERT INTO pool (code, depth, width, length, manager_id) VALUES (%s, %s, %s, %s, %s)",
                            (pool.code, pool.depth, pool.width, pool.length, pool.managerid))
            self.connection.commit()

        except Exception as e:
        # Handle exceptions
            print(f"Error: {e}")
        finally:
            return

    def addbracelet(self, brac):
        try:
            # Check if bracelet code exists
            self.cursor.execute("SELECT code FROM bracelet WHERE code = %s", (brac.code,))
            exist_code = self.cursor.fetchone()

            if exist_code:
                # Bracelet already exists
                return {"message": f"Bracelet with code {brac.code} already exists. You may want to update instead."}

            # Insert the new bracelet
            self.cursor.execute("INSERT INTO bracelet (code, customer_name, age) VALUES (%s, %s, %s)",
                                (brac.code, brac.customer_name, brac.age))
            self.connection.commit()
            return {"message": "The bracelet was added successfully."}

        except Exception as e:
            # Handle exceptions and return error message
            print(f"Error: {e}")
            return {"error": str(e)}

    def addmanager(self, manager):
        try:

            if not isinstance(manager.id, int):
                raise ValueError("Manager ID must be an integer")

            if manager.age is not None and not isinstance(manager.age, int):
                raise ValueError("Age must be an integer or None")

            if manager.salary is not None and not isinstance(manager.salary, int):
                raise ValueError("Salary must be an integer or None")


            self.cursor.execute("SELECT id FROM manager WHERE id = %s", (manager.id,))
            existing_id = self.cursor.fetchone()

            # Check if a manager with the same ID exists
            if existing_id:
                print( f"Manager with ID {manager.id} already exists. Consider updating instead.")
            else:
                # Insert the new manager
                print("Inserting new manager.")
                self.cursor.execute("INSERT INTO manager (id, age, name, salary) VALUES (%s, %s, %s, %s)",
                                    (manager.id, manager.age, manager.name, manager.salary))
                self.connection.commit()
                return {"message": f"Manager with ID {manager.id} added successfully."}

        except ValueError as ve:
            print(f"ValueError: {ve}")
            return {"error": str(ve)}
        except Exception as e:
            # Handle exceptions and rollback if there's an error
            self.connection.rollback()
            print(f"Error: {e}")
            return {"error": f"Error occurred: {e}"}
        finally:
            pass

    def findpoolbyid(self, poolcode):
        temp = None

        try:
            self.cursor.execute("SELECT code, depth, width, length, manager_id FROM pool WHERE code = %s", (poolcode,))
            pool = self.cursor.fetchone()

            if pool:
                temp = Pool( pool[1], pool[2], pool[3], pool[4])
            else :
                temp = None
        except Exception as e:
            print(f"error: {e}")

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
