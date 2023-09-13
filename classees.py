class Manager:
    id = 1
    def __init__(self , name = None , age = None , salary = None, headpools = None  ):
        super().__init__()
        self.id += 1
        self.age = age
        self.name = name
        self.salary = salary
        self.headpools = headpools if headpools is not None else []


    def __str__(self):
        return f'manager [id={self.id}, age={self.age}, name={self.name}, salary={self.salary}, ' \
               f'headpools={self.headpools}]'




class Pool:
    code=1
    def __init__(self, depth, width, length , costumersOfToday = None):
        super().__init__()
        self.depth = depth
        self.width = width
        self.length = length
        self.code += 1
        #the default value of costumersOfToday is none , if we passed actual list or cutomers we done, another
        # costumersOfToday equal to [] empty list
        self.costumersOfToday = costumersOfToday if costumersOfToday is not None else []
        self.manager = Manager()



    def __str__(self):
          man = "none" if self.manager.id == 0 else str(self.manager.id)
          return f"Pool [code={self.code}, depth={self.depth}, width={self.width}, length={self.length}, " \
                 f"costumers_of_today={self.costumersOfToday}, manager_code={man}]"





class kidspool(Pool):
    def __init__(self, depth, width, length , maxage , isneeded, costumersOfToday = None ):
        super().__init__(depth, width, length , costumersOfToday)
        self.maxage = maxage
        self.isneeded = isneeded

    def __str__(self):
        man = "none" if self.manager.id == 0 else str(self.manager.id)
        return f"Pool [code={self.code}, depth={self.depth}, width={self.width}, length={self.length}, " \
               f"costumers_of_today={self.costumersOfToday},maxage={self.maxage},isneeded={self.isneeded} manager_code={man}]"

class proffeional_pool(Pool):
    def __init__(self, depth, width, length, swimming_lines, olympicGamesNames = None ,costumersOfToday = None):
        super().__init__(depth, width, length, costumersOfToday)
        self.swimming_lines = swimming_lines
        self.olympicGamesNames = olympicGamesNames if olympicGamesNames is not None else []

    def __str__(self):
        return super().__str__() + f" a swimming lines are {self.swimming_lines} the olympic Games Names are {self.olympicGamesNames} "





class bracelet:
    code = 1
    def __int__(self, customer_name, pools_of_today=None ):
        super().__init__()
        self.customer_name=customer_name
        self.pools_of_today= pools_of_today if pools_of_today is not None else []

    def add_pool(self, pool):
        if pool is None:
            return False
        if pool in self.pools_of_today:
            return True
        self.pools_of_today.append(pool)
        return True
    def __str__(self):
        return f" bracelet is [the code is{self.code}, the name is {self.customer_name} , adn the visited pools are" \
               f" {self.pools_of_today}]"













