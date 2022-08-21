opp = input ("Insert Operator : ")
x = int(input("Insert First Number : "))
y = int(input("Insert Second Number : "))


if opp == "+":
    if x == 56 and y == 9:
        print ("Answer : 77")
    else:
        print ("Answer : ", x+y)
elif opp == "-":
    print ("Answer : ",x-y)
elif opp == "/":
    if x == 56 and y == 6:
        print ("Answer : 4")
    else:
        print ("Answer : ",x/y)
elif opp == "*":
    if x == 45 and y == 3:
        print ("Answer : 555")
    else:
        print ("Answer : ",x*y)