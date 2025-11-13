month = input("Enter the month: ").strip().capitalize()

# Determine the season
if month in ("September", "October", "November"):
    season = "Autumn"
elif month in ("December", "January", "February"):
    season = "Winter"
elif month in ("March", "April", "May"):
    season = "Spring"
elif month in ("June", "July", "August"):
    season = "Summer"
else:
    season = "Invalid month entered"

# Print the result
print(f"The season is {season}.")