# Dictionary containing other collections

engineer = {
    "name": "Bhushan",
    "location": "Bengaluru",
    "skills": [
        "Python",
        "CANoe",
        "UDS"
    ],
    "tools": [
        "PyCharm",
        "GitHub",
        "JIRA"
    ]
}

print("Engineer:", engineer)

print("Name:", engineer["name"])

print("Skills:", engineer["skills"])

print(
    "First Skill:",
    engineer["skills"][0]
)

print(
    "First Tool:",
    engineer["tools"][0]
)