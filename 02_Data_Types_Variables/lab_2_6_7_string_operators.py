leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)



# 2.6.6 Hypotenuse without intermediate variable
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

print("-" * 20) # Replication used as a divider

# 2.6.7 String Operators
print("Concatenation:", "ab" + "ba")
print("Replication:", "James" * 3)
print("Zero replication:", "Hello" * 0) # Outputs nothing



# 2.6.8 str() conversion
age = 21
# print("I am " + age + " years old.") # Uncomment to see TypeError
print("I am " + str(age) + " years old.")

# Drawing a simple rectangle using string operators
print("+" + "-" * 10 + "+")
print("|" + " " * 10 + "|")
print("+" + "-" * 10 + "+") 
# Summary: This lab practiced string concatenation and multiplication. 
# Note: Strings can be multiplied and concatenated easily. 
