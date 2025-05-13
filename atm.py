dictionary={}

while True:
    print("1: credit")
    print("2: withdraw")
    print("3: debit")
    print("4: exit")

    selection=int(input("selection the option:"))

    if selection==1:
        credit=input("enter the credit")
        print("credit successfully")

    elif selection==2:
        withdraw=input("enter the withdraw")
        print("withdraw successfully")

    elif selection==3:
        debit=input("enter the debit")
        print("debit successfully")

    elif selection==4:
        print("exit successfully")
        break