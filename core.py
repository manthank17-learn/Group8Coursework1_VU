"""
Core Business Logic for Personal Automation Hub
Enhanced version with advanced features and data structures
"""
import random
import datetime
from typing import Dict, List, Tuple, Union

# --- Enhanced Data Structures ---
DAILY_TASKS = {
    "Work": [
        "Check emails", 
        "Attend meetings", 
        "Complete project tasks", 
        "Review daily reports", 
        "Team standup",
        "Update project documentation",
        "Code review session",
        "Client communication",
        "Weekly planning",
        "Performance analysis"
    ],
    "Study": [
        "Review lecture notes", 
        "Complete assignments", 
        "Practice coding", 
        "Read course materials", 
        "Study group session",
        "Research project topics",
        "Prepare for exams",
        "Online course modules",
        "Academic writing",
        "Lab experiments"
    ],
    "Personal": [
        "Exercise", 
        "Meal prep", 
        "Call family", 
        "Read a book", 
        "Plan tomorrow",
        "Grocery shopping",
        "House cleaning",
        "Personal reflection",
        "Hobby time",
        "Social activities"
    ],
    "Creative": [
        "Write in journal", 
        "Learn new skill", 
        "Work on side project", 
        "Practice hobby", 
        "Brainstorm ideas",
        "Digital art creation",
        "Music practice",
        "Creative writing",
        "Photography session",
        "Design exploration"
    ]
}

MOTIVATIONAL_QUOTES = [
    "Work smarter, not harder. 💪",
    "Automate the boring stuff, enjoy life! 🚀",
    "One hour saved is one more for yourself tomorrow. ⏰",
    "Let technology work for you! 🤖",
    "Consistency beats intensity. Small steps daily! 📈",
    "Progress, not perfection. 🎯",
    "Your future self will thank you. 🙏",
    "Make it happen! ⚡",
    "Dream big, start small, move fast. 🏃‍♂️",
    "Success is automated habits. 🔄",
    "Innovation distinguishes between a leader and a follower. 🌟",
    "The best time to plant a tree was 20 years ago. The second best time is now. 🌳",
    "Don't wait for opportunity. Create it. 🔥",
    "Excellence is not a skill, it's an attitude. ✨",
    "The future belongs to those who believe in the beauty of their dreams. 🌈"
]

# Priority levels with their corresponding time multipliers
PRIORITY_CONFIG = {
    "High": {"emoji": "🔴", "multiplier": 1.5},
    "Medium": {"emoji": "🟡", "multiplier": 1.0},
    "Low": {"emoji": "🟢", "multiplier": 0.7}
}

# Time estimates for different types of tasks
TIME_ESTIMATES = ["15 min", "30 min", "45 min", "1 hour", "1.5 hours", "2 hours", "3 hours"]

# --- Core Functions ---

def generate_smart_todo(user_name: str, category: str = "Work", priority: str = "Medium") -> Tuple[List[str], str]:
    """
    Enhanced todo generator with categories, priorities, and time estimates
    
    Args:
        user_name (str): Name of the user
        category (str): Task category (Work, Study, Personal, Creative)
        priority (str): Priority level (High, Medium, Low)
    
    Returns:
        tuple: (enhanced_tasks, motivational_message)
    """
    if not user_name.strip():
        raise ValueError("User name cannot be empty")
    
    # Get tasks for the specified category
    base_tasks = DAILY_TASKS.get(category, DAILY_TASKS["Work"])
    
    # Select random tasks (3-5 tasks based on priority)
    num_tasks = 5 if priority == "High" else 4 if priority == "Medium" else 3
    num_tasks = min(num_tasks, len(base_tasks))
    selected_tasks = random.sample(base_tasks, num_tasks)
    
    # Enhance tasks with priority indicators and time estimates
    enhanced_tasks = []
    priority_config = PRIORITY_CONFIG[priority]
    
    for task in selected_tasks:
        # Select time estimate based on priority
        base_time_idx = random.randint(0, len(TIME_ESTIMATES) - 1)
        time_idx = min(len(TIME_ESTIMATES) - 1, 
                      int(base_time_idx * priority_config["multiplier"]))
        time_estimate = TIME_ESTIMATES[time_idx]
        
        enhanced_task = f"{priority_config['emoji']} {task} ({time_estimate})"
        enhanced_tasks.append(enhanced_task)
    
    # Select motivational message
    motivation = random.choice(MOTIVATIONAL_QUOTES)
    
    return enhanced_tasks, motivation

def advanced_financial_calc(salary: float, expenses: float, savings_goal: float = 0, 
                          currency: str = "UGX") -> Dict[str, Union[float, str]]:
    """
    Advanced financial calculator with comprehensive analysis
    
    Args:
        salary (float): Monthly salary
        expenses (float): Monthly expenses
        savings_goal (float): Target savings goal
        currency (str): Currency code
    
    Returns:
        dict: Comprehensive financial analysis results
    """
    if salary < 0 or expenses < 0 or savings_goal < 0:
        raise ValueError("Financial values cannot be negative")
    
    # Tax calculation (10% flat rate)
    tax_rate = 0.10
    tax = tax_rate * salary
    net_salary = salary - tax
    
    # Basic savings calculation
    savings = net_salary - expenses
    
    # Calculate percentages
    savings_rate = (savings / salary * 100) if salary > 0 else 0
    expense_rate = (expenses / salary * 100) if salary > 0 else 0
    tax_rate_percent = (tax / salary * 100) if salary > 0 else 0
    
    # Goal tracking
    months_to_goal = (savings_goal / savings) if savings > 0 and savings_goal > 0 else float('inf')
    
    # Future projections
    projected_savings_6m = savings * 6
    projected_savings_12m = savings * 12
    
    # Financial health indicators
    emergency_fund_needed = expenses * 6  # 6 months of expenses
    emergency_fund_coverage = (savings / expenses) if expenses > 0 else float('inf')
    
    # Debt-to-income ratio (assuming expenses include debt payments)
    debt_to_income = expense_rate
    
    # Financial health score (0-100)
    health_score = calculate_financial_health_score(savings_rate, debt_to_income, emergency_fund_coverage)
    
    return {
        'salary': salary,
        'tax': tax,
        'net_salary': net_salary,
        'expenses': expenses,
        'savings': savings,
        'savings_rate': savings_rate,
        'expense_rate': expense_rate,
        'tax_rate_percent': tax_rate_percent,
        'savings_goal': savings_goal,
        'months_to_goal': months_to_goal,
        'projected_savings_6m': projected_savings_6m,
        'projected_savings_12m': projected_savings_12m,
        'emergency_fund_needed': emergency_fund_needed,
        'emergency_fund_coverage': emergency_fund_coverage,
        'debt_to_income': debt_to_income,
        'health_score': health_score,
        'currency': currency
    }

def calculate_financial_health_score(savings_rate: float, debt_to_income: float, 
                                   emergency_coverage: float) -> float:
    """
    Calculate financial health score based on key metrics
    
    Args:
        savings_rate (float): Percentage of income saved
        debt_to_income (float): Debt to income ratio
        emergency_coverage (float): Months of emergency fund coverage
    
    Returns:
        float: Health score from 0-100
    """
    score = 0
    
    # Savings rate scoring (40 points max)
    if savings_rate >= 20:
        score += 40
    elif savings_rate >= 10:
        score += 30
    elif savings_rate >= 5:
        score += 20
    elif savings_rate > 0:
        score += 10
    
    # Debt-to-income scoring (30 points max)
    if debt_to_income <= 20:
        score += 30
    elif debt_to_income <= 30:
        score += 25
    elif debt_to_income <= 40:
        score += 15
    elif debt_to_income <= 50:
        score += 10
    
    # Emergency fund scoring (30 points max)
    if emergency_coverage >= 6:
        score += 30
    elif emergency_coverage >= 3:
        score += 20
    elif emergency_coverage >= 1:
        score += 10
    
    return min(100, score)

def smart_group_generator(names_str: str, group_size: int = 3, shuffle_mode: str = "Random") -> List[List[str]]:
    """
    Enhanced group generator with multiple algorithms and validation
    
    Args:
        names_str (str): Comma-separated string of names
        group_size (int): Desired size of each group
        shuffle_mode (str): Grouping algorithm (Random, Alphabetical, Reverse)
    
    Returns:
        list: List of groups, where each group is a list of names
    """
    if not names_str.strip():
        return []
    
    if group_size < 1:
        raise ValueError("Group size must be at least 1")
    
    # Parse and clean names
    names = [name.strip() for name in names_str.split(",") if name.strip()]
    
    if not names:
        return []
    
    # Remove duplicates while preserving order
    seen = set()
    unique_names = []
    for name in names:
        if name.lower() not in seen:
            seen.add(name.lower())
            unique_names.append(name)
    
    names = unique_names
    
    # Apply sorting based on shuffle mode
    if shuffle_mode == "Alphabetical":
        names.sort(key=str.lower)
    elif shuffle_mode == "Reverse":
        names.sort(key=str.lower, reverse=True)
    else:  # Random
        random.shuffle(names)
    
    # Create groups
    groups = []
    for i in range(0, len(names), group_size):
        group = names[i:i + group_size]
        groups.append(group)
    
    return groups

def generate_group_statistics(groups: List[List[str]]) -> Dict[str, Union[int, float, str]]:
    """
    Generate statistics about the created groups
    
    Args:
        groups (list): List of groups
    
    Returns:
        dict: Statistics about the groups
    """
    if not groups:
        return {
            'total_groups': 0,
            'total_members': 0,
            'average_size': 0.0,
            'size_distribution': {},
            'largest_group': 0,
            'smallest_group': 0
        }
    
    total_groups = len(groups)
    group_sizes = [len(group) for group in groups]
    total_members = sum(group_sizes)
    average_size = total_members / total_groups if total_groups > 0 else 0
    
    # Size distribution
    size_distribution = {}
    for size in group_sizes:
        size_distribution[size] = size_distribution.get(size, 0) + 1
    
    return {
        'total_groups': total_groups,
        'total_members': total_members,
        'average_size': round(average_size, 1),
        'size_distribution': size_distribution,
        'largest_group': max(group_sizes) if group_sizes else 0,
        'smallest_group': min(group_sizes) if group_sizes else 0
    }

def get_financial_advice(results: Dict) -> List[str]:
    """
    Generate personalized financial advice based on calculation results
    
    Args:
        results (dict): Results from advanced_financial_calc
    
    Returns:
        list: List of financial advice strings
    """
    advice = []
    savings_rate = results['savings_rate']
    health_score = results['health_score']
    
    # Savings rate advice
    if savings_rate < 10:
        advice.append("🎯 Try to increase your savings rate to at least 10% of your income.")
    elif savings_rate < 20:
        advice.append("📈 Good progress! Aim for 20% savings rate for optimal financial health.")
    else:
        advice.append("⭐ Excellent savings rate! You're building wealth effectively.")
    
    # Emergency fund advice
    emergency_coverage = results['emergency_fund_coverage']
    if emergency_coverage < 3:
        advice.append("🚨 Build an emergency fund covering 3-6 months of expenses.")
    elif emergency_coverage < 6:
        advice.append("💪 Good emergency fund! Consider extending it to 6 months.")
    else:
        advice.append("🛡️ Great emergency fund coverage! You're financially secure.")
    
    # Health score advice
    if health_score < 50:
        advice.append("⚠️ Focus on improving your financial habits for better stability.")
    elif health_score < 75:
        advice.append("📊 Your financial health is improving! Keep up the good work.")
    else:
        advice.append("🏆 Outstanding financial health! You're on track for success.")
    
    # Goal-specific advice
    if results['savings_goal'] > 0 and results['months_to_goal'] != float('inf'):
        months = results['months_to_goal']
        if months <= 12:
            advice.append(f"🎯 You'll reach your savings goal in {months:.1f} months!")
        else:
            advice.append(f"📅 Your savings goal will take {months:.0f} months. Consider increasing savings or adjusting the goal.")
    
    return advice

def validate_financial_inputs(salary: float, expenses: float, savings_goal: float = 0) -> Dict[str, str]:
    """
    Validate financial inputs and provide warnings
    
    Args:
        salary (float): Monthly salary
        expenses (float): Monthly expenses
        savings_goal (float): Target savings goal
    
    Returns:
        dict: Validation results with warnings
    """
    warnings = {}
    
    if salary <= 0:
        warnings['salary'] = "Salary must be greater than zero"
    
    if expenses < 0:
        warnings['expenses'] = "Expenses cannot be negative"
    
    if savings_goal < 0:
        warnings['savings_goal'] = "Savings goal cannot be negative"
    
    if expenses > salary:
        warnings['budget'] = "⚠️ Your expenses exceed your salary! Consider budgeting."
    
    expense_ratio = (expenses / salary * 100) if salary > 0 else 0
    if expense_ratio > 80:
        warnings['high_expenses'] = f"💸 High expense ratio ({expense_ratio:.1f}%). Consider reducing expenses."
    
    return warnings

def get_task_recommendations(category: str, completed_tasks: List[str] = None) -> List[str]:
    """
    Get task recommendations based on category and previously completed tasks
    
    Args:
        category (str): Task category
        completed_tasks (list): List of previously completed tasks
    
    Returns:
        list: Recommended tasks
    """
    if completed_tasks is None:
        completed_tasks = []
    
    all_tasks = DAILY_TASKS.get(category, DAILY_TASKS["Work"])
    
    # Filter out completed tasks
    available_tasks = [task for task in all_tasks if task not in completed_tasks]
    
    if not available_tasks:
        available_tasks = all_tasks  # Reset if all tasks completed
    
    # Return 3-5 recommended tasks
    num_recommendations = min(5, len(available_tasks))
    return random.sample(available_tasks, num_recommendations)

# --- Utility Functions ---

def format_currency(amount: float, currency: str = "UGX") -> str:
    """Format currency with proper symbols and formatting"""
    currency_symbols = {
        "UGX": "UGX ",
        "USD": "$",
        "EUR": "€",
        "GBP": "£"
    }
    
    symbol = currency_symbols.get(currency, currency + " ")
    
    if currency == "UGX":
        return f"{symbol}{amount:,.0f}"
    else:
        return f"{symbol}{amount:,.2f}"

def calculate_time_to_complete(tasks: List[str]) -> int:
    """
    Calculate estimated total time to complete all tasks (in minutes)
    
    Args:
        tasks (list): List of tasks with time estimates
    
    Returns:
        int: Total estimated minutes
    """
    total_minutes = 0
    
    for task in tasks:
        # Extract time from task string (assumes format: "task (X min)" or "task (X hour)")
        if "(" in task and ")" in task:
            time_part = task.split("(")[1].split(")")[0]
            
            if "hour" in time_part:
                hours = float(time_part.split()[0])
                total_minutes += int(hours * 60)
            elif "min" in time_part:
                minutes = int(time_part.split()[0])
                total_minutes += minutes
    
    return total_minutes

def get_productivity_tip() -> str:
    """Get a random productivity tip"""
    tips = [
        "🍅 Try the Pomodoro Technique: 25 minutes of focused work, then a 5-minute break.",
        "📝 Write down your tasks the night before to start your day with clarity.",
        "🎯 Focus on one task at a time to improve quality and efficiency.",
        "⏰ Use time blocking to allocate specific hours for different activities.",
        "🚫 Eliminate distractions by turning off notifications during focused work.",
        "💪 Take regular breaks to maintain high energy levels throughout the day.",
        "🎵 Use background music or white noise to enhance concentration.",
        "📱 Use apps and tools to automate repetitive tasks.",
        "🌅 Tackle your most challenging task when your energy is highest.",
        "📊 Track your time to understand where you spend it most."
    ]
    
    return random.choice(tips)

# --- Data Export Functions ---

def export_financial_summary(results: Dict) -> str:
    """
    Export financial analysis as a formatted string
    
    Args:
        results (dict): Financial calculation results
    
    Returns:
        str: Formatted financial summary
    """
    summary = f"""
📊 FINANCIAL ANALYSIS SUMMARY
{'='*40}

💰 Income & Deductions:
   Gross Salary: {format_currency(results['salary'], results['currency'])}
   Tax (10%): {format_currency(results['tax'], results['currency'])}
   Net Salary: {format_currency(results['net_salary'], results['currency'])}

💸 Expenses & Savings:
   Monthly Expenses: {format_currency(results['expenses'], results['currency'])}
   Monthly Savings: {format_currency(results['savings'], results['currency'])}
   Savings Rate: {results['savings_rate']:.1f}%

📈 Projections:
   6-Month Savings: {format_currency(results['projected_savings_6m'], results['currency'])}
   12-Month Savings: {format_currency(results['projected_savings_12m'], results['currency'])}

🎯 Financial Health Score: {results['health_score']:.0f}/100

Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    return summary.strip()

# --- Constants for Analytics ---

ANALYTICS_METRICS = {
    'features_used': ['todo_generator', 'financial_calculator', 'group_generator'],
    'user_engagement': ['daily_active', 'weekly_active', 'monthly_active'],
    'performance_indicators': ['task_completion_rate', 'user_satisfaction', 'feature_adoption']
}

# --- Version Information ---
__version__ = "2.0.0"
__author__ = "Group No. 8"
__description__ = "Enhanced Personal Automation Hub with advanced features"
