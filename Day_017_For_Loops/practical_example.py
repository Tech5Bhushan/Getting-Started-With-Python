# Practical Example
# Processing Test Results

test_results = {
    "TC_101": "PASS",
    "TC_102": "FAIL",
    "TC_103": "PASS",
    "TC_104": "FAIL"
}

passed = 0
failed = 0

for test_case, status in test_results.items():

    print(
        "Processing:",
        test_case,
        "-",
        status
    )

    if status == "PASS":
        passed += 1

    elif status == "FAIL":
        failed += 1


print("\nTest Summary")
print("----------------")
print("Total:", len(test_results))
print("Passed:", passed)
print("Failed:", failed)