import copy


list=[
    [10,20,30],
    [40,50,60]
]

lst1=copy.copy(list)
print(lst1)

lst2=copy.deepcopy(list)

print(lst2)
