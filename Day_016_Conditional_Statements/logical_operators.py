# Logical Operators with Conditions

age = 25
has_license = True

# and
if age >= 18 and has_license:
    print("Can drive")


# or
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# not
is_logged_in = False

if not is_logged_in:
    print("Please login")