a=int(input("Enter a number: "))
if a%2==0:
    if a%3==0:
        print(a,"is divisible by 2 and 3")
    else:
        print(a,"is divisible by 2 but not by 3")
else:
    print(a,"is  not divisible by 2 and 3")

