days = int(input("How may days would you like to convert to minutes? "))  # Takes user input for days as an integer
minutesInDay = (days * 24 * 60) # Calculates the number of minutes in the given number of days
print(f"There are " + str(minutesInDay) + " minutes in " + str(days) + " days.") # Prints the number of minutes in the given number of days