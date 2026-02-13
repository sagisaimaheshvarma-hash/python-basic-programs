b=int(input("enter no of days present: "))
a=int(input("enter total no of working days: "))
percentage=(b/a)*100
if percentage>=75:
    print(percentage,"allowed to sit in exam")
else:
    print(percentage,"not allowed to sit in exam")