

from classees import *


if __name__ == '__main__':
    customers = ["Customer1", "Customer2", "Customer3"]
    pool1 = Pool(5.0, 10.0, 20.0, customers)
    man = Manager("anotone",32,34534,pool1)
    # man1 = Manager("sally", 33, 343)
    kidypool= kidspool(5.0, 10.0, 20.0, 15, True, customers)
    propool= proffeional_pool(5.0, 10.0, 20.0, 15,[],["Customer1", "Customer2", "Customer3"])

    print(propool)



    print(pool1.code)
    pool1.manager = man
    # pool1.manager = man1
    pool1.costumersOfToday.append("semaa")
    print(pool1)
    print(man)
    print(kidypool)
    print((pool1.manager))












