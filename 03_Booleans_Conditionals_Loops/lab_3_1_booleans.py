# --- 3.1.6 LAB: Variables - Questions and answers ---
print("--- LAB 3.1.6 ---")
n = int(input("Enter a number: "))
# The lab asks for a two-line program without if statements. 
# We just print the result of the comparison directly.
print(n >= 100)

# --- 3.1.7 Conditional Execution Examples ---
print("\n--- 3.1.7 Examples ---")

# Simple if
weather = "good"
if weather == "good":
    print("Go for a walk")

# If-else
weather = "bad"
if weather == "good":
    print("Go for a walk")
else:
    print("Go to the theater")

# If-elif-else cascade
print("\n--- Cascade Example ---")
tickets = False
table = True

if tickets:
    print("Go to theater")
elif table:
    print("Go to lunch")
else:
    print("Play chess at home")