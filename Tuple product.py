tup1 = (4,3,2,2,-1,18)
tup2 = (2,4,8,8,3,2)

lentup = len(tup1)
tuple_product = ()
product = ()

for i in range(lentup):
    tuple_product = (tup1[i]*tup2[i])
    print(tuple_product)