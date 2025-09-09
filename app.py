import streamlit as st
import random
import datetime

# --- Data ---
Daily_task = ("Check emails", "Attend class/meetings", "Complete 3 coding exercises")
Motivational_messages = (
    "Work Smarter, not harder.",
    "Automate the boring stuff, Enjoy your life!",
    "One hour saved is one more for yourself Tomorrow.",
    "Let technology Work for you!",
    "Consistency beats intensity. Small steps daily!"
)

# --- Coursework Intro (Hard-coded group info) ---
st.title("🚀 Coursework 1 - Personal Automation Hub")

st.markdown("""
## 👥 Group No. 8  

- **AKELLO PRISCILLA** — VU-BBC-2503-0802-DAY  
- **Manthan Kumar** — VY-BBC-2503-0494-DAY  
- **Ainembabazi Ollen** — VU-BSF-2503-0047-DAY  
- **Najjemba Sarah Leon** — VU-BBC-2503-2377-DAY  
- **ASIIMWE ROGERS PRAISE** — VU-DIT-2503-0111-DAY  

---

📖 **Coursework Question**  
*In groups of not more than three (5), develop a creative python program that incorporates concepts covered in the class.*  
*Note: All group members must participate to ensure full mark for all.*  
""")

# --- Functions ---
def generate_todo_list(user_name):
    tasks = Daily_task
    message = random.choice(Motivational_messages)
    return tasks, message

def calculate_savings(salary, expenses):
    tax = 0.10 * salary
    savings = salary - tax - expenses
    return savings, tax

def random_groups(names_str):
    names = [n.strip() for n in names_str.split(",") if n.strip()]
    random.shuffle(names)
    return [names[i:i+3] for i in range(0, len(names), 3)]

# --- Sidebar Menu ---
st.sidebar.header("📌 Menu")
choice = st.sidebar.radio(
    "Choose an option:",
    ["Intro", "To-Do List", "Salary Savings", "Random Groups"]
)

# --- Main Section ---
if choice == "Intro":
    st.subheader("Welcome to Coursework 1")
    st.info("This project demonstrates automation, randomization, and financial calculations using Python and Streamlit.")

elif choice == "To-Do List":
    user_name = st.text_input("Enter your name:")
    if st.button("Generate"):
        tasks, message = generate_todo_list(user_name)
        st.success(f"📅 To-Do list for {datetime.date.today()}")
        for i, t in enumerate(tasks, 1):
            st.write(f"{i}. {t}")
        st.info(f"✨ Motivation: {message}")

elif choice == "Salary Savings":
    salary = st.number_input("Enter your monthly salary:", min_value=0.0, step=100.0)
    expenses = st.number_input("Enter your monthly expenses:", min_value=0.0, step=50.0)
    if st.button("Calculate"):
        savings, tax = calculate_savings(salary, expenses)
        st.success(f"💰 Tax: {tax} UGX | Savings: {savings} UGX")

elif choice == "Random Groups":
    names = st.text_area("Enter student names (comma separated):")
    if st.button("Generate Groups"):
        groups = random_groups(names)
        for i, g in enumerate(groups, 1):
            st.write(f"👥 Group {i}: {', '.join(g)}")

