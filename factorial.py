#Program to calculate factorial of a given number
def get_factorial(num):
    
    ans = 1

    for i in range (1,num+1):
        ans = ans*i
    
    #print("factoraial of a given number is :", ans)
    return ans

print(get_factorial(5))