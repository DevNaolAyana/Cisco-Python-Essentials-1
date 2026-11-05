# Lab 2.1.5 - Working with the print() function

# Step 1 & 2: Print greeting and name
print("Hello, Python!")
print("Naol")

# --- EXPERIMENTS (Uncomment one at a time to see the errors) ---

# Step 3: Missing quotes (Causes SyntaxError)
# print(Hello, Python!)

# Step 4: Missing parentheses (Causes SyntaxError)
# print"Hello, Python!"

# Step 5: Experiments
print('Single quotes work too')
print("Same line"); print("Another line")
print("Multiple", "arguments", "here")

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