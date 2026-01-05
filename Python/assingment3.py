# a=5
# b=10
# sum=a+b

# normal formatting
# print("sum is {}".format(sum))

# index-based formatting
# print("sum of {1} AND {0} is{2}".format(a,b,sum))

# value-based formatting
# print("values of vars {a} and {b}".format(a=5,b=10))


#Given a list of tuples with info(name,Subject):
# list all unique Course
# list students enrolled in english
# create dictionary (student,set Of courses)

# info=[
#     ("Alice","Math"),
#     ("Bob","Science"),
#     ("Alice","Science"),
#     ("Charlie","Math"),
#     ("Bob","Math"),
#     ("Alice","English"),
#     ("Charlie","English"),
# ]

# unique_course=set()

# for tup in info:
#     unique_course.add(tup[1])
# print(unique_course)

# for name,course in info:
#     if(course=="English"):
#         print(name)

# dict={}
# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)

# print(dict)

#Asktheuserforastringandcheckwhetheritisapalindromeornot

# Str=input("Enter the String")

# clean=Str.replace(" ","").lower()
# if(clean==clean[::-1]):
#     print("the String is Palindrome")
# else:
#     print("The String is not Palindrome")

# Givenalistofintegerscomputetheaverageofallnumbersinthelist
# list=[20,50,4,7,5]
# sum=0

# for i in list:
#     sum=sum+i

# print(sum/len(list))

## Input first list
# list1 = list(map(int, input("Enter first list elements separated by space: ").split()))

# Input second list
# list2 = list(map(int, input("Enter second list elements separated by space: ").split()))

# Merge and sort
# result = sorted(list1 + list2)

# print("Merged and Sorted List:", result)

# Givenatupleofintegers,create:Q4•Atupleofallevennumbers•Atupleofalloddnumbers

# numbers=tuple(map(int,input("Enter the Numbers").split()))

# even=tuple(num for num in numbers if num%2==0)
# odd=tuple(num for num in numbers if num%2!=0)

# print(even)
# print(odd)

# students = {}

# while True:
#     print("\n----- MENU -----")
#     print("A. Add a student")
#     print("B. Update marks")
#     print("C. Search for a student")
#     print("D. Display all students and marks")
#     print("E. Exit")

#     choice = input("Enter your choice (A/B/C/D/E): ").upper()

    
#     if choice == "A":
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students[name] = marks
#         print("Student added successfully!")

    
#     elif choice == "B":
#         name = input("Enter student name to update: ")
#         if name in students:
#             marks = int(input("Enter new marks: "))
#             students[name] = marks
#             print("Marks updated successfully!")
#         else:
#             print("Student not found!")

    
#     elif choice == "C":
#         name = input("Enter student name to search: ")
#         if name in students:
#             print(f"{name}'s marks: {students[name]}")
#         else:
#             print("Student not found!")

    
#     elif choice == "D":
#         if students:
#             print("\nStudent Records:")
#             for name, marks in students.items():
#                 print(f"{name} : {marks}")
#         else:
#             print("No records available.")

   
#     elif choice == "E":
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice! Please select A, B, C, D, or E.")







# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# word_length_dict = {}

# for word in words:
#     word_length_dict[word] = len(word)

# print(word_length_dict)



# text = input("Enter a string: ")

# space_count = text.count(" ")

# print("Number of spaces in the string:", space_count)
