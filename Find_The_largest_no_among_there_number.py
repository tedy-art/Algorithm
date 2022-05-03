"""
step 1: start
step 2: Declare variables a, b, and c
step 3: Read variables a, b, and c
step 4: If a>b
            If a > c
                Display a is the largest number
            Else
                Display c is the largest number
        Else
            If b > c
                Display b is the largest number
            Else
                Display c is the greatest number
step 5: stop
"""
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

if a > b:
    if a > c:
        print("a is the largest number.")
    else:
        print("c is the largest number.")
else:
    if b > c:
        print("b is the largest number.")
    else:
        print("c is the gratest number.")