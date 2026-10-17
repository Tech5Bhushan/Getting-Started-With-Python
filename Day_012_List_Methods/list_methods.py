# Day 12 - List Methods in Python

# append()
languages = ["Python", "Java"]
languages.append("C++")
print("After append:", languages)

# extend()
languages.extend(["JavaScript", "C#"])
print("After extend:", languages)

# insert()
languages.insert(1, "Go")
print("After insert:", languages)

# remove()
languages.remove("Java")
print("After remove:", languages)

# pop()
removed_language = languages.pop(2)
print("Removed element:", removed_language)
print("After pop:", languages)

# index()
position = languages.index("C++")
print("Index of C++:", position)

# count()
skills = ["Python", "CANoe", "Python", "Git"]
print("Python count:", skills.count("Python"))

# sort()
numbers = [40, 10, 30, 20]
numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

# reverse()
tools = ["CANoe", "PyCharm", "GitHub"]
tools.reverse()
print("Reversed tools:", tools)

# copy()
copied_tools = tools.copy()
copied_tools.append("JIRA")

print("Original tools:", tools)
print("Copied tools:", copied_tools)

# clear()
languages.clear()
print("After clear:", languages)