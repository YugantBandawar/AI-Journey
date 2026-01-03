# Writeaprogramthattakesasinput.Usingconditionalstatements,calculatethebasedontheserules:
# Q1salaryfinaltaxrate•Ifsalary<30,000→5%
# Ifsalaryis30,000–70,000→15%
# •Ifsalary>70,000→25%

# salary=float(input("Enter the Salary:"))
# if salary<30000:
#     print("The Final Tax is:", 0.05*salary)

# elif salary>30000 and salary<70000:
#     print("The Final Tax is:", 0.15*salary)

# else:
#     print("The final Salary is:", 0.25*salary)    


# Write a function that takes two integers a and b prints all even numbers between them

# a=int(input("Enter First digit:"))
# b=int(input("Enetr the second digit:"))

# def Even(a,b):
#     for i in range(a,b):
#         if(i%2==0):
#             print(i)

# Even(a,b)

# Write a function that prints the of a number,.digits n For eg 342:,there are 3 digits in it 3,1and2 & we need to print them

# def print_digits(n):
#     digits = []
#     n = abs(n)

#     while n > 0:
#         digits.append(n % 10)
#         n //= 10

#     for d in reversed(digits):
#         print(d)

# print_digits(312)


#Write a function to return the count the number of digits in anumber ,n.

# def count_digits(n):
#     if n==0:
#         return 1
#     count=0
#     n=abs(n)
#     while n>0:
#         count+=1
#         n//=10
#     return count
# ans=count_digits(312)
# print(ans)

#Write a function to return the sum of a number

# def sum(n):
#     if(n==0):
#         return 0
    
#     sum=0
#     while(n>0):
#         sum=sum+n
#         n=n-1
#     return sum
# ans=sum(10)
# print(ans)


#Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

# for i in range(1,100):
#     if(i%15==0):
#         print(i)

# Design a program to continuously input a number n from user &print if it is positive or negative until the user enters “Quit”

# while True:
#     n=input("Enter the number or Quit")
#     if(n=="Quit"):
#         print("Program has been Terminated")
#         break
    
#     n=float(n)
#     if(n>0):
#         print("The number is positive")
#     elif n<0:
#         print("The number is negative")

#     elif n==0:
#         print("The number is Zero")

#     else:
#         print("Invalid input")
        
        
        


    

