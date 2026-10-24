# Practical Example
# Simulating ECU Connection Retry Logic

attempt = 1
max_attempts = 3
ecu_connected = False

while attempt <= max_attempts:

    print(
        "Connection attempt:",
        attempt
    )

    # Simulated connection result
    # The connection succeeds on attempt 3.
    if attempt == 3:
        ecu_connected = True

    if ecu_connected:
        print("ECU Connected")
        break

    print("Connection Failed")

    attempt += 1


if not ecu_connected:
    print(
        "Unable to connect after",
        max_attempts,
        "attempts"
    )