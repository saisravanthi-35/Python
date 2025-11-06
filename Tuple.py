myTuple = ("A","B","C")
tuple1 = (1,3,"Abc")
for x in tuple1:
    print(x)
tuple2 = (1)
tuple3 = (2, "hii",4.6,2.3)
print(type(tuple2))
print(type(tuple3))                       #same as List
print(len(tuple3))
print(tuple3[1])
print(tuple3[-1])
print(tuple3[2:])
print(tuple3[:3])
n = len(myTuple)
i = 0
while i<n:
    print(myTuple[i])
    i+=1


tupleA = ("a","b","c","a")
tupleB = (1,3,5)
print(tupleA+tupleB)

tupleC = tupleA*2
print(tupleC)

print(tupleA.count("a"))
print(tupleA.index("a"))