#ask for age
#18-21  wristband
#21+ drink, normal entry
#too young , sorry
print("enter your age here :")
age = input()
if age == None or age=='':
    print("Please enter your age")
    age = input()
else:
    agef = float(age)
    if agef > 21:
        print("drink normal")
    elif agef >= 18 or agef<21:
        print("wristband")
    else:
        print("too young , sorry")