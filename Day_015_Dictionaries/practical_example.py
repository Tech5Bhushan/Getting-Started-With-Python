# Practical Example
# Representing a test execution result

test_result = {
    "test_id": "TC_101",
    "requirement": "WI-41845",
    "status": "Passed",
    "execution_time": 12.5,
    "automated": True
}

print("Test Result")

print(
    "Test ID:",
    test_result["test_id"]
)

print(
    "Requirement:",
    test_result["requirement"]
)

print(
    "Status:",
    test_result["status"]
)

print(
    "Execution Time:",
    test_result["execution_time"]
)

print(
    "Automated:",
    test_result["automated"]
)