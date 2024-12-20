#Using for loop, write and run a Python program to find factorial from 0 to 10.

def function(num):
    fact = 1
    for i in range(1, num + 1):
        fact= fact * i
    print(f"The factorial of {num} is {fact}")       

function(1)
function(2)
function(3)
function(4)
function(5)
function(6)
function(7)
function(8)
function(9)
function(10)