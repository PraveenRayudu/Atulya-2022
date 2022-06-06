str=input("enter numbers and strings:")
sum = 0
for c in str:
    if c.isdigit() == True:
        sum = sum + int(c)
print(sum)