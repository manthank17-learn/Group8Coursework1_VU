import random
import datetime

# --- Data ---
Daily_task = (
    "Check emails",
    "Attend class/meetings",
    "Complete 3 coding exercises"
)

Motivational_messages = (
    "Work Smarter, not harder.",
    "Automate the boring stuff, Enjoy your life!",
    "One hour saved is one more for yourself Tomorrow.",
    "Let technology Work for you!",
    "Consistency beats intensity. Small steps daily!"
)

# --- Functions ---

def generate_todo_list(user_name: str):
    """
    Generates a to-do list for the user along with a random motivational message.
    Returns: (tasks, message)
    """
    tasks = Daily_task
    message = random.choice(Motivational_messages)
    return tasks, message


def calculate_savings(salary: float, expenses: float):
    """
    Automates salary -> tax -> savings calculation.
    Returns: (savings, tax)
    """
    tax = 0.10 * salary
    savings = salary - tax - expenses
    return savings, tax


def random_groups(names_str: str):
    """
    Randomly divides students into groups of 3.
    names_str: comma-separated string of names
    Returns: list of groups (each group is a list of names)
    """
    names = [n.strip() for n in names_str.split(",") if n.strip()]
    if not names:
        return []
    random.shuffle(names)
    return [names[i:i+3] for i in range(0, len(names), 3)]
