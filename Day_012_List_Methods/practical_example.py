# Practical example: Managing test tools

test_tools = ["CANoe", "PyCharm", "GitHub"]

print("Initial tools:", test_tools)

# Add one tool
test_tools.append("JIRA")

# Add a tool at a specific position
test_tools.insert(1, "CANalyzer")

# Safely remove an existing tool
tool_to_remove = "PyCharm"

if tool_to_remove in test_tools:
    test_tools.remove(tool_to_remove)

# Arrange tools alphabetically
test_tools.sort()

print("Updated tools:", test_tools)
print("Number of tools:", len(test_tools))