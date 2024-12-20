list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


result = [a + b for a in list1 for b in list2]

print(result)