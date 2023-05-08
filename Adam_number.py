def is_adam_number(n):
    # Calculate square of n
    square_n = n * n
 
    # Get the reverse of n
    rev_n = int(str(n)[::-1])
 
    square_rev_n = rev_n * rev_n
 
    rev_square_rev_n = int(str(square_rev_n)[::-1])
 
    return square_n == rev_square_rev_n
 
 
n = int(input())
if is_adam_number(n):
    print("True")
else:
    print("False")
