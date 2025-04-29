#map(funnction,iterable,....)
list_1=[25,45,67,58,96,10,58]
def square(a):
    return a**2
result=map(square,list_1)
print(list(result))

def add(a,b):
    return a+b
print(add(25,45))

result=lambda a,b,c:a+b+c
print(result(2,3,4))

result=lambda a,b,c,d:a*b*c*d
print(result(5,6,7,8))

list_2=[55,77,9,84,76,10,2]
result=filter(lambda a:a%2==0,list_2)
print(list(result))

list_3=[45,67,88,99,2,4]
empty_list=[]
for i in list_3:
    result=i**2

    empty_list.append(result)
print(empty_list)

list_1=[25,45,22,58,96,10,55,1,2,36,79,24]
def square(a):
    return a**2
result=map(square,list_1)
print(list(result))

list_4=[1,3,4,5]
def square(a):
    return a**2
result=map(square,list_4)
print(list(result))

def sample():
    yield 1 python or hold
    yield 2 hold or hold
    yield 3 hold or hold
    def=sample()
print(obj.-next-())






