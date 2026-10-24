# Looping through different Python collections


# List

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)


# Tuple

tools = ("CANoe", "PyCharm", "GitHub")

for tool in tools:
    print(tool)


# Set
# Do not rely on iteration order.

skills = {"Python", "CANoe", "Git"}

for skill in skills:
    print(skill)


# Dictionary

test_result = {
    "test_id": "TC_101",
    "status": "PASS",
    "automated": True
}

for key, value in test_result.items():
    print(key, ":", value)