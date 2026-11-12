# # name = input("Enter a plant name: ")

# # if name == "Spathiphyllum":
# #     print("Yes - Spathiphyllum is the best plant ever!")
# # elif name == "spathiphyllum":
# #     print("No, I want a big Spathiphyllum!")
# # else:
# #     print(f"Spathiphyllum! Not {name}!")


# income = float(input("Enter the annual income: "))

# if income <= 85528:
#     tax = (income * 0.18) - 556.02
# else:
#     tax = 14839.02 + ((income - 85528) * 0.32)

# # If tax is less than 0, make it 0
# if tax < 0:
#     tax = 0.0

# # Round to full thalers (0 decimal places)
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")




year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")