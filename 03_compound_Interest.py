# Take principle, tenure and interest rate from user and prints compound interest and total sum
def calculate_compound_interest():

    # input parameters are taken in integer format
    principal = int(input("Enter principle amount: "))
    tenure = int(input("Enter tenure in years: "))
    interest_rate = int(input("Enter interest rate: "))

    interest = principal * ((1 + interest_rate/100) ** tenure - 1)

    #result display
    print("compound interest is", interest, "and total sum after compounding is", principal+interest)

calculate_compound_interest()