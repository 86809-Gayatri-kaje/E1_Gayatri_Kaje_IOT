# #The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F


num1 = int(input("Enter ECP marks  : "))
num2 = int(input("Enter DSA marks : "))
num3 = int(input("Enter RTOS marks : "))
avg = (num1 + num2 + num3)/3

if avg >=90:
    print("GRADE :: A")
    
elif avg>=80 and avg<90:
    print("Grade : B ")

elif avg>=70 and avg<80:
    print("Grade : C ")

elif avg>=60 and avg<70:
    print("Grade : D ")        
    
else:
    print("Grade : E ")

print(f"Avg marks is = {avg}")
