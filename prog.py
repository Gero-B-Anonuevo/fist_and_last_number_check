#pseudocode
#ask the numbers
first_number = int(input("What is your first number: "))
second_number = int(input("What is your second number: "))
third_number = int(input("What is your third number: "))
fourth_number = int(input("What is your fourth number: "))
fifth_number = int(input("What is your fifth number: "))

print("Given list: [", first_number, ", ", second_number, ", ", third_number, ", ", fourth_number, ", ", fifth_number, "]")

#compare first and last given number
#true if identical and false if not
if first_number == fifth_number:
    print("Result is: True")
else:
    print("Result is: False")