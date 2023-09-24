
from classees import *


if __name__ == '__main__':
    p1=  Pool(2 ,2 ,5)
    p2 = Pool(3, 2, 5)
    p3 = Pool(2, 2, 5)

#     here you should add to data strucre

    pp1= proffeional_pool(2,2,5,4)
    pp2= proffeional_pool(3,5,5,4)
    pp3= proffeional_pool(7,5,7,8)

#     add to datasystem
    pp1.olympicGamesNames.append("xx1")
    pp1.olympicGamesNames.append("xx2")

    pp2.olympicGamesNames.append("yy2")
    pp2.olympicGamesNames.append("yy3")

    pp3.olympicGamesNames.append("tt1")
    pp3.olympicGamesNames.append("tt2")


#     add to datasystem


    kp1= kidspool(0.3,3,5,3,True)
    kp2= kidspool(0.7,5,5,6,False)
    kp3= kidspool(2,5,7,16,False)

#     add to datasystem


    b1= bracelet('Oscar Pistorius')
    b2= bracelet("Svetlana Romashina")
    b3= bracelet("Katie Ledecky")


#     add to datasystemD



    p1.costumersOfToday.append(b1)
    p1.costumersOfToday.append(b2)
    b1.pools_of_today.append(p1)
    b2.pools_of_today.append(p1)

    p2.costumersOfToday.append(b1)
    p2.costumersOfToday.append(b3)
    b1.pools_of_today.append(p2)
    b3.pools_of_today.append(p2)

    p3.costumersOfToday.append(b2)
    p3.costumersOfToday.append(b1)
    b1.pools_of_today.append(p3)
    b2.pools_of_today.append(p3)


    pp1.costumersOfToday.append(b1)
    pp1.costumersOfToday.append(b2)
    b1.pools_of_today.append(pp1)
    b2.pools_of_today.append(pp1)

    pp2.costumersOfToday.append(b2)
    pp2.costumersOfToday.append(b3)
    b3.pools_of_today.append(pp2)
    b2.pools_of_today.append(pp2)

    pp3.costumersOfToday.append(b1)
    b1.pools_of_today.append(pp3)

    kp1.costumersOfToday.append(b1)
    kp1.costumersOfToday.append(b1)
    b1.add_pool(kp1)
    b2.add_pool(kp1)

    kp2.costumersOfToday.append(b2)
    b2.add_pool(kp2)

    kp3.costumersOfToday.append(b2)
    kp3.costumersOfToday.append(b1)
    b2.add_pool(kp3)
    b1.add_pool(kp3)


    m1= Manager("martin",47,13000)
    m2 = Manager("alex", 37, 11000)\



#     add the mamgers to the datasystem


    m1.headpools.append(p1)
    m1.headpools.append(pp1)
    m1.headpools.append(kp1)
    m2.headpools.append(p2)
    m2.headpools.append(pp3)

    p1.manager=m1
    pp1.manager=m1
    kp1.manager=m1
    p2.manager=m2
    pp3.manager=m2



#     add the (ppool.cpde, manager) to the appropiate hashtable for(pool, manager)









































