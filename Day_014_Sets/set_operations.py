# Set Operations

testing_tools = {"CANoe", "JIRA", "Python"}
development_tools = {"Python", "GitHub", "PyCharm"}

# Union
all_tools = testing_tools.union(development_tools)
print("Union:", all_tools)

# Intersection
common_tools = testing_tools.intersection(development_tools)
print("Intersection:", common_tools)

# Difference
testing_only = testing_tools.difference(development_tools)
print("Testing only:", testing_only)

# Symmetric difference
different_tools = testing_tools.symmetric_difference(
    development_tools
)
print("Symmetric difference:", different_tools)