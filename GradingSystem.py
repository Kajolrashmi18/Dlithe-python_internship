'''
Write a program to calculate the grade. The grade should be calculated in the following method.

Constraints 
Score should be in between 1 to 100

Score
	>= 90	 --> Grade O
	>= 80	--> Grade A+
	>= 70	--> Grade A
	>= 60	--> Grade B+
	>= 50	--> Grade B
	< 50	No Grade
  '''


grade = int(input("Enter the marks : "))

if grade>=90 and grade<=100:
    print("Your Grade is O")
elif grade>=80 and grade<90:
    print("Your Grade is A+")
elif grade>=70 and grade<80:
    print("Your Grade is A")
elif grade>=60 and grade<70:
    print("Your Grade is B+")
elif grade>=50 and grade<60:
    print("Your Grade is B")
elif grade<50:
    print("No Grade")
else:
    print("Invalid Input!")
