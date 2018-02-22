def fibonacci_series(number):
    a = 0
    b = 1

    print(a, b, end=" ")

    while number >= 1:
        a, b = b, a + b
        number -= 1

        print(b, end=" ")


inputNumber = int(input("Enter number till where you want to generate Fibonacci series.. \n"))
fibonacci_series(inputNumber)
