

from classees import *


if __name__ == '__main__':
    customers = ["Customer1", "Customer2", "Customer3"]
    pool1 = Pool(5.0, 10.0, 20.0, customers)
    man = Manager("anotone",32,34534,pool1)
    kidypool= kidspool(5.0, 10.0, 20.0, 15, True, customers)


    print(pool1.code)
    pool1.manager = man
    print(pool1)
    print(man)
    print(kidypool)












