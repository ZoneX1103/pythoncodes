a = int(input("Enter your number: \n"))

prime = True

for i in range(2, a):
    if(a % i == 0):
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")