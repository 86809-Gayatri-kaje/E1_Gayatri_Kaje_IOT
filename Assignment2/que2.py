# #Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
# ut should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639

num = int(input("Enter 4 digit number"))
n1 = int(num/1000)
n2 = int((num/100)%10)
n3 = int((num/10)%10)
n4 = int(num%10)

print(f"{n1} {n2} {n3} {n4}")
print(f"{n1*1000} {n2*100} {n3*10} {n4}")
print (f"{n4} {n3} {n2} {1}")