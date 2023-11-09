from classees import *


class database:
    def __init__(self, pools_list=None, managers_list=None, code_brac_dic=None, poolcode_manager_dic=None):
        self.pools_list = pools_list if pools_list is not None else []
        self.managers_list = managers_list if managers_list is not None else []
        self.code_brac_dic = code_brac_dic if code_brac_dic is not None else {}
        self.poolcode_manager_dic = poolcode_manager_dic if poolcode_manager_dic is not None else {}

    def addpool(self, pool):
        if pool is None:
            return False
        if pool in self.pools_list:
            return False

        if isinstance(pool, Pool):
            self.pools_list.append(pool)
            return True

    def addmanager(self, manager):
        if manager is None:
            return False
        if manager in self.managers_list:
            return False

        if isinstance(manager, Manager):
            self.managers_list.append(manager)
            return True

    def addbracelet(self, brac):
        if brac is None:
            return

        if brac in self.code_brac_dic:
            return

        if isinstance(brac, bracelet):
            self.code_brac_dic[brac.code] = brac

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
                p= self.findpoolbyid(pcode)
                i+= 1
                toreturn.append(p)
                print(f" {i}. {p}")

        if pcode == 0:
            print(f"this manager does not has any pools that he manage")

        return toreturn















        




