import subprocess

def run_script(script_name):
    """Run a specified Python script."""
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

def main():
    while True:  # Loop to keep asking for user input
        print("\nSelect a program to run:")
        print("1. Script One")
        print("2. Script Two")
        print("3. Script Three")
        print("4. Script Four")
        print("5. Exit")  # New exit option
        
        choice = input("Enter your choice (1-5): ")

        scripts = {
            '1': 'vulnerability_scanner.py',
            '2': 'system_status.py',
            '3': 'malware_remover.py',
            '4': 'network_scanner.py'
        }

        if choice in scripts:
            run_script(scripts[choice])
        elif choice == '5':
            print("Exiting the program.")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
