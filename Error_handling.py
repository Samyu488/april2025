#ValueError

num_1=int(input("enter the number1:"))
num_2=int(input("enter the number2:"))
try:
    print(num_1*num_2)
except ValueError as e:
    print(e)

 #zeroerror
 
num_1=int(input("enter the number1:"))
num_2=int(input("enter the number2:"))
try:
    print(num_1/num_2)
except ZeroDivisionError as e:
    print(e)

num_1=int(input("enter the number1:"))
num_2=int(input("enter the number2:"))
try:
    print(num_1/num_2)
except Exception as e:
    print(e)


    


          


