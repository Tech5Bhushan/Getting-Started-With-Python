# Practical Example
# Test Execution Decision

ecu_connected = True
environment_ready = True

if ecu_connected and environment_ready:
    print("Start Test Execution")
else:
    print("Test Preconditions Not Met")


# Test Result Evaluation

test_status = input(
    "Enter test status (PASS/FAIL): "
).strip().upper()

if test_status == "PASS":
    print("Test Case Passed")

elif test_status == "FAIL":
    print("Test Case Failed")

else:
    print("Invalid Test Status")