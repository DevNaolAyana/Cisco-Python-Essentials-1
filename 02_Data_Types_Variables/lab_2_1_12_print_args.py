
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")



print("The itsy bitsy spider\nclimbed up the waterspout.")
print("\\") # Prints one backslash


# Changing 'end' to a space (so the next print joins the same line)
print("My name is", end=" ")
print("Monty Python.")

# Changing 'sep' to a dash
print("My", "name", "is", "Monty", "Python.", sep="-")


print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# 1. Making the arrow twice as large and duplicating it side by side
arrow = "\n    *\n   ***\n  *****\n *******"
print(arrow * 4)

# 2. Breaking it (uncomment to see errors)
# print("    *)  # SyntaxError: unterminated string literal
# Print("Hello") # NameError: name 'Print' is not defined 
# Summary: This lab used sep and end to format output. 
# Note: Practice using sep and end parameters together. 
