av = 6
x = int(input("Enter the no.of candies:"))

i  = 1
while i <= x:
    if i > av:
        print("out of stock")
        break
    print("candies")
    i = i + 1
print("Bye")