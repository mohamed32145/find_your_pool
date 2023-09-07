

from pool import Pool


if __name__ == '__main__':
    customers = ["Customer1", "Customer2", "Customer3"]
    pool1=Pool(5.0, 10.0, 20.0, customers)
    print(pool1.code)


