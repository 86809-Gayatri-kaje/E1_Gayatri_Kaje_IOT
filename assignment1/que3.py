#Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard.

a = [10, 24, 76, 23, 12]
largest = a[0]
for val in a:
  if val > largest:
    largest = val
print(largest)