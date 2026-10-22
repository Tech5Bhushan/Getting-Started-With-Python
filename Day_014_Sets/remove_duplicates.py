# Removing duplicate values using a Set

skills = [
    "Python",
    "CANoe",
    "Python",
    "Git",
    "CANoe"
]

unique_skills = set(skills)

print("Original List:", skills)
print("Unique values:", unique_skills)

# Convert the Set back into a List
unique_skills_list = list(unique_skills)

print("Unique List:", unique_skills_list)