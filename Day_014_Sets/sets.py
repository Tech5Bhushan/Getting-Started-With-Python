# Day 14 - Sets in Python

# Creating a Set
languages = {"Python", "Java", "C++"}

print("Languages:", languages)


# Duplicate values are automatically removed
skills = {"Python", "CANoe", "Python", "Git"}

print("Unique skills:", skills)


# Add one element
languages.add("JavaScript")

print("After add:", languages)


# Add multiple elements
languages.update(["C#", "Go"])

print("After update:", languages)


# Remove an existing element
languages.remove("Java")

print("After remove:", languages)


# Safely remove an element
languages.discard("Rust")

print("After discard:", languages)


# Membership testing
print("Python exists:", "Python" in languages)
print("Ruby exists:", "Ruby" in languages)


# Set length
print("Number of languages:", len(languages))


# Empty Set
empty_set = set()

print("Empty Set:", empty_set)
print("Type:", type(empty_set))