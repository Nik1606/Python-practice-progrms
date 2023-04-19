# function take two numbers from user and print their sum
def print_sum():
    num1 = input("Enter first number here: ")
    num2 = input("Enter second number here: ")

    #convert input from int to float and then print sum
    sum = float(num1) + float(num2)
    print("sum of ", num1, "and", num2, "is", sum)


print_sum()