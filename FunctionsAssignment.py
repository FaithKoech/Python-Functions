# Practice questions: PART A: practice question
# We should create a function that ‘findsgrade’ by
# taking in marks of each subject as parameters
# calculating total from the parameters(subjects) passed
# calculating the average from the total
# using if statement to find grade
# what if I want to get total marks! and average?
# def my_score():
#     Scores=[]
#     print("Enter Your Score for each Subject:")
#     for i in range(5):
#         Score = input("Subj " + str(i + 1) +":")
        # Scores.append(int(score))
        # TotalMarks=sum(Scores)/5
        # print(TotalMarks)
# my_score()




# practice question 2
# Write a function called sum_digits that is given an integer num and returns the sum of the digits of num.
# def sum_digits(num):
#     Sum=0
#     while num>0:
#







# Practice questions: PART B
# TASK 1:
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
# Hint: Use input () to get the persons input
# print("Do you Love Python?")
# Answer=input("Enter Yes or No:")
# if Answer == "Yes":
#     print("Yes")
# else: print("No")



# TASK 2:
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.

# def max_three():
#     num1 =float(input("Enter the First No:"))
#     num2 =float(input("Enter the Second No:"))
#     num3 =float(input("Enter the Third No:"))
#     if (num1>=num2) and (num1>=num3):
#         Largest =num1
#     elif (num2>=num1) and (num2>=num3):
#         Largest=num2
#     else:
#         Largest=num3
#         print("The Largest is: ", Largest)
# max_three()




# TASK 3:
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function

# def new_list():
#     l=list()
#     for i in range(1,21):
#         l.append(i**2)
#         print(l[:5])
# new_list()




# TASK 4:
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# number = input("Enter a number: ")
# if int(number) % 2 == 0:
#     print(str(number) + " is an Even number.")
# else:
#     print(str(number) + " is an Odd number.")
# if int(number) % 4 == 0:
#     print(str(number) + " is a multiple of 4")
# num = input("Enter first number > ")
# check = input("Enter 2nd Number > ")
# if int(num) % int(check) == 0:
#     print(str(num) + " divides evenly by " + str(check)+".")
# else:
#     print(str(num) + " does NOT divide evenly by " + str(check)+".")






# TASK 5:
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.


tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple1 = tuple[:5]
tuple2=tuple[:5]
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple1=tuple[:5]
# tuple2=tuple[5:]
print(tuple1)
print(tuple2)







# MILESTONE TASK
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary.
# NB: Use KRA, NHIF and NSSF values provided in the link below.
