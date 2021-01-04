def collatz(number):
    if number % 2 == 0: # if even
        result = number // 2
    else: # if odd
        result = 3 * number + 1
    print(result)
    return result

current_number = int(input('Please input an integer:\n'))
while current_number != 1:
    current_number = collatz(current_number)