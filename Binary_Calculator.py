print(
    """
      Binary Calculator
      """
)

a = int(input("Please Enter a Number Between 0 and 255: "))

if a <= 255:
    if a >= 128:
        a = a - 2**7
        b1 = "1 "
    else:
        b1 = "0 "

    if a >= 64:
        a = a - 2**6
        b2 = "1 "
    else:
        b2 = "0 "

    if a >= 32:
        a = a - 2**5
        b3 = "1 "
    else:
        b3 = "0 "

    if a >= 16:
        a = a - 2**4
        b4 = "1 "
    else:
        b4 = "0 "

    if a >= 8:
        a = a - 2**3
        b5 = "1 "
    else:
        b5 = "0 "

    if a >= 4:
        a = a - 2**2
        b6 = "1 "
    else:
        b6 = "0 "

    if a >= 2:
        a = a - 2
        b7 = "1 "
    else:
        b7 = "0 "

    if a == 1:
        b8 = "1"
    else:
        b8 = "0"

    print(b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + "\n")
else:
    print(
        "You entered a number larger than 255, so it cannot be calculated in a byte\n"
    )

if a == 1:
    print("Odd Number")
else:
    print("Even Number")
