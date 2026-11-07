print(2 ** 3)       # 8
print(5 / 2)        # 2.5
print(4 / 2)        # 2.0 (Always float!)
print(5 // 2)       # 2
print(-5 // 2)      # -3 (Rounds down to the lesser integer!)
print(12 % 4.5)     # 3.0
print(4 % -8)       # -2

print(2 + 3 * 5)        # 17 (* comes before +)
print(9 % 6 % 2)        # 1 (Left-to-right)
print(2 ** 2 ** 3)      # 256 (Right-to-left!)
print(-3 ** 2)          # -9 (Exponentiation before unary minus)
print(2 * 3 % 5)        # 1 (Left-to-right: 2*3=6, 6%5=1)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # 2.0


# Basic Operators
print("Basic:", 2 + 2, 5 - 2, 3 * 3)
print("Exponent:", 2 ** 3)
print("Division:", 5 / 2, 4 / 2)
print("Floor Div:", 5 // 2, -5 // 2)
print("Modulo:", 5 % 2, 12 % 4.5, 2 % -4)

# Priorities and Bindings
print("Priority:", 2 + 3 * 5)
print("Left Binding:", 9 % 6 % 2)
print("Right Binding:", 2 ** 2 ** 3)
print("Unary vs Power:", -3 ** 2)
print("Complex:", (5 * ((25 % 13) + 100) / (2 * 13)) // 2)