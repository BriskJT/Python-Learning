#-------------------------------------------------
# Day 4: Revising and cleaning up the code from Day 3
# - Swapped kit grade and name input
# - Removed lambda function and replaced with named functions for sorting
# - Improved function and variable names
#-------------------------------------------------

# List of allowed grades
grades = ["HG", "RG", "MG", "MGEX", "MGSD", "PG", "PGU"]

# Orders the grades manually for output
grade_order = {
    "HG": 1,
    "RG": 2,
    "MG": 3,
    "MGEX": 4,
    "MGSD": 5,
    "PG": 6,
    "PGU": 7
}

# ---Functions for input prompts---
# Maximum number of kits allowed in the list
max_kits = 99

# A function to prompt user for kit grades
def prompt_for_grade():
    """
    Prompts the user to enter the grade of an unbuilt kit they own. Ensures valid input. 
    Normalizes input to uppercase, and strips whitespace. 
    Returns the valid grade.
    """
    while True:
        grade = input ("Enter grade (HG, RG, RG, MGEX, MGSD, PG, PGU) "
                       "or press Enter to finish: ").strip().upper()
        if grade == "":      # the user pressed Enter to finish
            return None
        if grade in grades:  # valid input
            return grade
        else:
            print("Invalid grade. Please choose from the given choices.")

# A function to prompt user for kit names
def prompt_for_kits():
    """
    Prompts the user to enter the names of unbuilt kits they own. 
    Empty input ends the process.
    Returns a list of kit names.
    """
    name = input("Enter the name of an unbuilt kit you own (or press Enter to finish): ").strip()
    return name

# ---Functions for sorting and displaying kit output---
# Functions to sort the backlog list
def sort_key(kit: tuple[str, str]) -> tuple[int, str]:
    """
    A fucntion to help generate the sort key for each kit.
    Sorts first by grade according to grade_order, then alphabetically by kit name.
    """
    grade, name = kit
    return (grade_order.get(grade, 99), name.lower())

def sort_backlog(backlog: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """
    Sorts the backlog by grade priority and kit name.
    Returns a sorted list of kits.
    """
    return sorted(backlog, key=sort_key)

# A function to display the backlog
def display_backlog(backlog: list[tuple[str, str]]):
    """
    Displays the backlog list in a formatted manner.
    """
    count = len(backlog)
    print("\n" + "-" * 99)
    print(f"You have {count} unbuilt kit(s) in your backlog.")
    print("-" * 99)
    if count == 0:
        print("Your backlog is empty.")
        return

# ---Loops for collecting kit data---
# # Main backlog list
def collect_backlog() -> list[tuple[str, str]]:
    """
    Main loop to collect unbuilt kit names and grades from the user.
    Stops when the user enters an empty name or reaches max_kits.
    For each, prompts for the kit name and grade, and appends to the backlog list.
    Returns the completed backlog list.
    """
    backlog: list[tuple[str, str]] = []

    print("Welcome to the Kit Backlog Collector!")
    print(f"You can enter up to {max_kits} unbuilt kits.")
    print("To finish entering kits, just press Enter without typing a name.\n")

    while len(backlog) < max_kits:
        #ask for kit name
        grade = prompt_for_grade()

        # Check for empty input to end
        if grade is None:
            print("Ending kit entry.")
            break

        # Ask for kit grade
        name = prompt_for_kits()
        if name == "":
            print("Ending kit entry.")
            break

        # Add to list as a tuple (kit_name, kit_grade)
        backlog.append((grade, name))

        # Display current count
        remaining = max_kits - len(backlog)
        print(f"Added: [{grade}] {name}. You can add {remaining} more kit(s).\n")

        # Loop ended or max kits reached
    return backlog

# ---Main program execution---
if __name__ == "__main__":
    backlog = collect_backlog()
    ordered_backlog = sort_backlog(backlog)
    for idx, (grade, name) in enumerate(ordered_backlog, start=1):
        print(f"{idx}. [{grade}] {name}")