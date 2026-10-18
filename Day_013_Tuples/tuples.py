# Day 13 - Tuples in Python

# Creating a Tuple
languages = ("Python", "Java", "C++")

print("Tuple:", languages)


# Positive indexing
print("First:", languages[0])
print("Second:", languages[1])


# Negative indexing
print("Last:", languages[-1])


# Slicing
languages = ("Python", "Java", "C++", "JavaScript")

print("Slice:", languages[1:3])


# Tuple length
print("Number of languages:", len(languages))


# Duplicate values
skills = ("Python", "CANoe", "Python", "Git")

print("Skills:", skills)
print("Python count:", skills.count("Python"))


# index()
tools = ("CANoe", "PyCharm", "GitHub")

print("PyCharm index:", tools.index("PyCharm"))


# Mixed data types
person = ("Bhushan", 34, 5.9, True)

print("Person:", person)


# Single-element Tuple

not_a_tuple = ("Python")
single_tuple = ("Python",)

print(type(not_a_tuple))
print(type(single_tuple))