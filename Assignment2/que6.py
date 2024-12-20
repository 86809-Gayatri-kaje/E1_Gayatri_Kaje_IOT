#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def function(num):
    fact = 1
    for i in range(1, num + 1):
        fact= fact * i
    print(f"The factorial of {num} is {fact}")       

function(5)
function(9)