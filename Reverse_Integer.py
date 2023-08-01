def reverse_integer(number):
    negative = False
    if number < 0:
        negative = True
        number = abs(number)
    reversed_str = str(number)[::-1]
    reversed_number = int(reversed_str)
    if negative:
        reversed_number = -reversed_number
    
    return reversed_number
try:
    num_input = int(input())
    reversed_num = reverse_integer(num_input)
    print(reversed_num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
