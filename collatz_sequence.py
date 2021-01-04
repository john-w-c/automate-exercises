def collatz(number):
    if number % 2 == 0:
        result = number //2
        print(result)
    else:
        result = 3 * number + 1
        print(result)
    return result

    