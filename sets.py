#set union

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.union(set2)
print(set3)

#set intersection

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

#set difference

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.difference(set2)
print(set3)

#set symmetric difference
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3= set1.symmetric_difference(set2)
print(set3)

#set membership test
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.isdisjoint(set2)
print(set3)

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5}
set3 = set1.issubset(set2)
print(set3)

#Exercise1 :set intersection
set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,}
set3 = set1.intersection(set2)
print(set3)

#Exercise2 :set union
set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,}
set3 = set1.union(set2)
print(set3)

#Execrise3:set diffrence
set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,}
set3 = set1.difference(set2)
print(set3)

#Execrise4:set symmetric difference
set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,}
set3 = set1.symmetric_difference(set2)
print(set3)