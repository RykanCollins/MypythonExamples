number = 0

def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    
    elif number % 2 ==1:
        return (3 * number + 1)
try:
    while collatz(number) != 1:
        number = int(input("enter number: "))
        print (collatz(number))
except ValueError:
    print("Must be an interger")
    #number = int(input("enter number: "))

    
