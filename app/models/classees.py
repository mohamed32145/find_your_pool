
class Manager:
    def __init__(self, id, name=None, age=None, salary=None, headpools=None):
        super().__init__()
        self.id = id

        # Validate that age is either None or an integer
        if age is not None and not isinstance(age, int):
            raise ValueError("Age must be an integer or None")
        self.age = age

        # Validate that salary is either None or an integer
        if salary is not None and not isinstance(salary, int):
            raise ValueError("Salary must be an integer or None")
        self.salary = salary

        self.name = name
        self.headpools = headpools if headpools is not None else []

    def add_pool(self, pool):
        if pool is None:
            return False
        if pool in self.headpools:
            return True
        self.headpools.append(pool)
        return True

    def __eq__(self, other):
        if isinstance(other, Manager):
            return self.id == other.id
        return False

    def __str__(self):
        temp = [p.code for p in self.headpools]
        return f'manager [id={self.id}, age={self.age}, name={self.name}, salary={self.salary}, ' \
               f'headpools={temp}]'



class Pool:
    code = 1

    def __init__(self, depth, width, length, managerid):
        super().__init__()
        self.depth = depth
        self.width = width
        self.length = length
        self.code = Pool.code
        self.managerid= managerid
        Pool.code += 1



    def __str__(self):
        return f"Pool [code={self.code}, depth={self.depth}, width={self.width}, length={self.length}, " \
               f" manager_code={self.managerid}]"


class kidspool(Pool):
    def __init__(self, depth, width, length, maxage, managerid,  isneeded):
        super().__init__(depth, width, length, managerid)
        self.maxage = maxage
        self.isneeded = isneeded

    def __str__(self):
        # man = "none" if self.manager.id == 0 else str(self.manager.id)
        parent_str = super().__str__()
        child_str = f" maxage={self.maxage},isneeded={self.isneeded} "
        return parent_str + child_str


class proffeional_pool(Pool):
    def __init__(self, depth, width, length,managerid, swimming_lines, olympicGamesNames=None):
        super().__init__(depth, width, length, managerid)
        self.swimming_lines = swimming_lines
        self.olympicGamesNames = olympicGamesNames if olympicGamesNames is not None else []

    def __str__(self):
        return super().__str__() + f" a swimming lines are {self.swimming_lines} the olympic Games Names are {self.olympicGamesNames}"


class bracelet:
    def __init__(self, code,customer_name, age, pools_of_today=None):
        super().__init__()
        self.customer_name = customer_name
        self.pools_of_today = pools_of_today if pools_of_today is not None else []
        self.age = age
        self.code = code


    def add_pool(self, pool):
        if pool is None:
            return False
        if pool in self.pools_of_today:
            return True
        self.pools_of_today.append(pool)
        return True

    def __str__(self):
        temp = [p.code for p in self.pools_of_today]
        return f" bracelet is [the code is {self.code}, the name is {self.customer_name} ,the age is {self.age} " \
               f"and the visited pools are" \
               f" {temp}]"
