#list methode

#--extend() method
l1=[1,2,3,6,7,8,9,7,50,15]
l2=[40,80,98,10,85,45,458,458,426,4502] 
l1.extend(l2)
print(l1)
#--append() methode
l1.append("skander")
l1.pop(-1)
print(l1)
#---sort() methode
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
#--count() methode
#counting how many time anelemt accure in the list
print(l1.count(458))
#--index() methode
print(l1.index(458))
#--insert() methode it takes 2 parm index and item 
l1.insert(l1.index(458),79)
print(l1)
#-- pop() methode it take the index of the elemt and return the variable deleted
x=l1.pop(2)
print(l1)
print(x)
#--remove() methode
l1.remove(458)
print(l1)
#--delete() methode , you can delete an elemt or a complet list
del l1,l2
#print(l1)

#---------------------------------------------------------------------------------------------------------------------------------
#tuple
numbers=(12,54.8,78,86,48.3,86)
print(numbers)
for x in numbers:
    print(x)
print(numbers[2])
numbers2=tuple((15,12,6,48,98,74,58))
print(numbers2)
print(len(numbers2))
#------------------------------------------------------------------------------------------------------------------------------
#set
""" you can add a value to a set but you can't change an exsisting value """
numb={1,5,8,4,9,96,58,4}
print(numb)

numb2=set((45,25,9,8,7,5,9,6282,9,5,695,65,2652))
print(numb2)
print(len(numb2))
numb2.add(55)
numb2.update([12,548,759,4855,488756,464846431,0])
print(numb2)
numb2.remove(55)
print(numb2)
numb2.clear()
print(numb2)
#-------------------------------------------------------------------------------------------------------------------------
#--dictionary, rhe values can be changed but values are unique
dic={"item":10,"sknader":152}
dic2=dict(skander=15,veg="apple")
print(dic2)
dic2['year']=2021
print(dic2)
#-- get methode
print(dic2.get("year"))
#--update
dic2.update({"skander":59})
print(dic2)
#--key
keys=dic2.keys()
print(keys)
#--values
values=dic2.values()
print(values)
#pop
x=dic2.pop("skander")
print(dic2,x)
dic2.clear()
print(dic2)
del dic2