a = int(input("Enter your number you want to see their multiplicative table:\n"))

i = 0

print("The multiplicative table of your given number is: \n")

for i in range(1, 11):
    print(str(a) + " X " + str(i) + " = " + str(a * i))