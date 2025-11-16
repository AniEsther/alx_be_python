# daily_reminder.py

# Loop to allow input validation
while True:
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    if task == "":
        print("Task cannot be empty. Please enter a valid task.")
        continue

    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter high, medium, or low.")
        continue

    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no for time-bound.")
        continue

    # Input is valid; exit loop
    break

# Process reminder based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)