
print("how many times do i have to tell you clean up your house")
yail = int(input())

for shout in range(yail):
    if shout == 4 or shout == 13:
        print("Unlucky number")
    elif shout % 2 == 0:
        print("even")
    else:
        print("old")

