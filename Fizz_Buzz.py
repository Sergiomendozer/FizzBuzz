for n in range(0, 21):
    if n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 != 0 and n % 5 != 0:
        print(n)
