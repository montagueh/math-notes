from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

x = symbols("x")

y_string = input("Input the x value for the function y = x: ")
y = parse_expr(y_string)

range_start_string = input("Enter beginning of the range for x: ")
range_start = parse_expr(range_start_string)
range_end_string = input("Enter the end of the range for x: ")
range_end = parse_expr(range_end_string) + 1

for i in range(range_start, range_end):
    print(f"x = {i}: y = {y.subs(x, i)}")
