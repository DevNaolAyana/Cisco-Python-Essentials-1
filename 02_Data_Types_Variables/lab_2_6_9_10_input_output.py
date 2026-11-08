print("--- LAB 2.6.9: Simple input and output ---")
# The lab asks for four basic operations. We will input two numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) # Note: will crash if b is 0





print("\n--- LAB 2.6.10: Operators and expressions ---")
# The expression is: 1 / (x + 1 / (x + 1 / (x + 1 / x)))
x = float(input("Enter a value for x: "))

# It's best to use parentheses to ensure the order of operations is correct
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)