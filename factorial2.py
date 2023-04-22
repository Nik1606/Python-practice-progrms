#This program calculates factorial of a given number by using WHILE loop
def get_factorial(num):
    ans = 1
    while num > 0:
        ans = ans*num
        num -= 1

    return ans

print(get_factorial(5))