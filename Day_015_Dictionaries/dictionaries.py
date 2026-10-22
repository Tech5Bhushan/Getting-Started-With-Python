# Day 15 - Dictionaries in Python

# Creating a Dictionary
person = {
    "name": "Bhushan",
    "age": 34,
    "city": "Bengaluru",
    "skill": "Python"
}

print("Dictionary:", person)


# Accessing values
print("Name:", person["name"])
print("City:", person["city"])


# Using get()
print("Skill:", person.get("skill"))

print(
    "Company:",
    person.get("company", "Not Available")
)


# Adding a new entry
person["language"] = "English"

print("After adding:", person)


# Updating a value
person["skill"] = "Python Automation"

print("After updating:", person)


# Dictionary length
print("Number of entries:", len(person))


# Keys
print("Keys:", person.keys())


# Values
print("Values:", person.values())


# Items
print("Items:", person.items())


# Removing an entry
removed_city = person.pop("city")

print("Removed city:", removed_city)
print("Updated Dictionary:", person)