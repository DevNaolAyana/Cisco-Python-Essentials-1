hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# 1. Calculate new minutes
# The % 60 ensures the minutes stay within 0-59
end_mins = (mins + dura) % 60



# 2. Calculate how many extra hours we gained from the minutes
extra_hours = (mins + dura) // 60

# 3. Calculate new hours
# We add extra_hours, then use % 24 to wrap around midnight if needed
end_hours = (hour + extra_hours) % 24

# 4. Print the result
print(end_hours, ":", end_mins, sep="") 
# Summary: This lab calculated end times using modulo. 
