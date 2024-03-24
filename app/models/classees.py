class Manager:
    id = 1

    def __init__(self, name=None, age=None, salary=None, headpools=None):
        super().__init__()
        self.id = Manager.id
        Manager.id += 1
        self.age = age
        self.name = name
        self.salary = salary
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

    def __init__(self, depth, width, length, costumersOfToday=None):
        super().__init__()
        self.depth = depth
        self.width = width
        self.length = length
        self.code = Pool.code
        Pool.code += 1
        # the default value of costumersOfToday is none , if we passed actual list or cutomers we done, another
        # costumersOfToday equal to [] empty list
        self.costumersOfToday = costumersOfToday if costumersOfToday is not None else []
        self.manager = Manager()

    def add_customer(self, brac):
        if brac is None:
            return False
        if brac in self.costumersOfToday:
            return True
        self.costumersOfToday.append(brac)
        return True

    def __str__(self):
        temp = [b.code for b in self.costumersOfToday]
        man = "none" if self.manager.id == 0 else str(self.manager.id)
        return f"Pool [code={self.code}, depth={self.depth}, width={self.width}, length={self.length}, " \
               f"costumers_of_today={temp}, manager_code={man}]"


class kidspool(Pool):
    def __init__(self, depth, width, length, maxage, isneeded, costumersOfToday=None):
        super().__init__(depth, width, length, costumersOfToday)
        self.maxage = maxage
        self.isneeded = isneeded

    def __str__(self):
        # man = "none" if self.manager.id == 0 else str(self.manager.id)
        parent_str = super().__str__()
        child_str = f" maxage={self.maxage},isneeded={self.isneeded} "
        return parent_str + child_str


class proffeional_pool(Pool):
    def __init__(self, depth, width, length, swimming_lines, olympicGamesNames=None, costumersOfToday=None):
        super().__init__(depth, width, length, costumersOfToday)
        self.swimming_lines = swimming_lines
        self.olympicGamesNames = olympicGamesNames if olympicGamesNames is not None else []

    def __str__(self):
        return super().__str__() + f" a swimming lines are {self.swimming_lines} the olympic Games Names are {self.olympicGamesNames}"


class bracelet:
    code = 1

    def __init__(self, customer_name, age, pools_of_today=None):
        super().__init__()
        self.customer_name = customer_name
        self.pools_of_today = pools_of_today if pools_of_today is not None else []
        self.age = age
        self.code = bracelet.code
        bracelet.code += 1

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
