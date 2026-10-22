# Practical example:
# Comparing failures from two test runs

run_1_failures = {
    "TC_101",
    "TC_102",
    "TC_105"
}

run_2_failures = {
    "TC_102",
    "TC_104",
    "TC_105"
}

common_failures = run_1_failures.intersection(
    run_2_failures
)

all_failures = run_1_failures.union(
    run_2_failures
)

only_run_1 = run_1_failures.difference(
    run_2_failures
)

only_run_2 = run_2_failures.difference(
    run_1_failures
)

print("Run 1 failures:", run_1_failures)
print("Run 2 failures:", run_2_failures)
print("Common failures:", common_failures)
print("All unique failures:", all_failures)
print("Only in Run 1:", only_run_1)
print("Only in Run 2:", only_run_2)