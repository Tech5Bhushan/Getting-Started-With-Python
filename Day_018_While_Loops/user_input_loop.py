# Repeat until the user enters "exit"

command = ""

while command != "exit":

    command = input("Enter command (type exit to stop): ").strip().lower()

    if command != "exit":
        print("You entered:", command)

print("Program stopped")