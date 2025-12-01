from analyzer import analyze_password
from wordlist import generate_wordlist
from gui import launch_gui

if __name__ == "__main__":
    launch_gui()


def menu():
    print("\n==== PASSWORD SECURITY TOOL ====")
    print("1. Analyze Password Strength")
    print("2. Generate Custom Wordlist")
    print("3. Exit")
    return input("Choose option: ")

while True:
    choice = menu()

    if choice == "1":
        pwd = input("Enter password to analyze: ")
        analyze_password(pwd)

    elif choice == "2":
        name = input("Enter Name: ")
        dob = input("Enter DOB (e.g. 2002): ")
        pet = input("Enter Pet Name: ")
        generate_wordlist(name, dob, pet)

    elif choice == "3":
        print("Exiting... Done.")
        break
    else:
        print("Invalid option. Try again.")
