"""Swap Two Variables
Take two numbers and swap their values without using a third variable."""


a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

print(f"\nBefore swapping: a = {a}, b = {b}")


a, b = b, a

print(f"After swapping:  a = {a}, b = {b}")
