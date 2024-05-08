## Display menu
def display_menu():
    print("Help")
    print("=" * 4)
    print("The following commands are recognized:")
    print("Display help")
    print("Exit the application")

# Debugging the display_menu() function
display_menu()

## User input

def display_menu():
    print("Help")
    print("=" * 4)
    print("The following commands are recognized:")
    print("Display help")
    print("Exit the application")

def main():
    while True:
        command = input("wildlife> ")

        if command == "help":
            display_menu()
        elif command == "exit":
            print("Exiting the application...")
            break
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")

if __name__ == "__main__":
    main()
