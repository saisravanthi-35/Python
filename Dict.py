mydict = {
    "A": 1,
    "B": 2,
    "C":True,
    "D": 3.8,
    20:"hello",
    21:"hello",
    "mylist":[1,2,3]
}
"""mydict2 = mydict.copy()
mydict2 = dict(mydict)
print(mydict)
mydict["A"] = 111
print(mydict)
print(mydict2)"""
"""mydict["X"]= "hello"
mydict.update({"P": 100})   #it will add the new elements
print(mydict)"""

"""mydict.pop("A")
mydict.popitem()
print(mydict)"""

"""del mydict["D"]
del mydict
print(mydict)"""

#mydict.clear()
#print(mydict)

#for x in mydict:
    #print(mydict[x])
#for x,y in mydict.items():
    #print(x,y)

#if "A" in mydict:
    #print("yes")
#else:
   # print("No") 

#print(mydict)
#print(len(mydict))
#print(mydict["C"])

#y= mydict["B"]
#z = mydict.get("B")
#print(z)
#print(y)

"""allkey = mydict.keys()
print(allkey)
mydict["b"] = 11
allkey2 = mydict.keys()
print(allkey2)
print(mydict["b"])"""

allvalues = mydict.values()
y = allvalues
print(y)

mydict["B"] = 56          #reference by value

allitems = mydict.items()
print(allitems)