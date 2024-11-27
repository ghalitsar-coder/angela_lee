import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.functions import calc_operator

# def is_leap_year(year):
#     # Write your code here.
#     #year =2000 #n(n-1) = 500 = 0 = true       #n(n-1) = 100 =  0 =false    #n(n-1)= 400 = true
#     #year =2001 #n(n-1) = 501 = 1 = false       #n(n-1) = 101 =  1 =true    #n(n-1)= 401 = false
#     print(f"{year%4}")
#     return (year % 4 == 0 and year % 100 != 0 ) or (year % 400 ==0)
#     # Don't change the function name.


# def is_leap_year(year: int):
#     """Fungsi yg bertujuan untuk mencari apakah tahun yang dimasukan
#     adalah tahun yang memiliki 366 hari atau bukan"""
#     # Step 1: Check if the year is divisible by 400
#     if year % 400 == 0:
#         return True

#     # Step 2: Check if the year is divisible by 100
#     if year % 100 == 0:
#         return False

#     # Step 3: Check if the year is divisible by 4
#     if year % 4 == 0:
#         return True

#     # Step 4: If none of the above, it's not a leap year
#     return False


# print(is_leap_year(int(input("Input Year : "))))


def calculator():
    """Kalkulatoorr wakwaww  angka"""
    result = 0
    keep_counting = False
    while True:
        first_num = int(input("First Number : ")) if not keep_counting else result
        operation = input("Which Operation \n+\n-\n/\n*\n :  ")
        second_num = int(input("Whats the next Number : "))
        print(f"current  first number {first_num}")
        result = calc_operator(operation, first_num, second_num)
        print(f"Result : {first_num} {operation} {second_num} = {result}")
        cont = input(
            f"Do you want to continue with {result} ? y for yes and n to start new calculation and out for out the calculation : "
        ).lower()
        if cont == "y":
            keep_counting = True
        elif cont == "n":
            result = 0
            keep_counting = False
        else:
            print("See you later !")
            break


calculator()
