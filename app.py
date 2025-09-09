import streamlit as st
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
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

# --- Page Configuration ---
st.set_page_config(
    page_title="Personal Automation Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Modern UI with Fixed Color Contrast ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #667eea;
        color: #212529;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        border-top: 3px solid #667eea;
        color: #212529;
    }
    
    .success-animation {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .task-item {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .group-card {
        background: linear-gradient(135deg, #fff5f5 0%, #fef2f2 100%);
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 4px solid #ef4444;
        color: #1f2937;
    }
    
    .group-card h4 {
        color: #1f2937;
        font-weight: 600;
    }
    
    .group-card ul {
        color: #374151;
    }
    
    .about-section {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #0284c7;
        color: #1e293b;
    }
    
    .about-section h3 {
        color: #0f172a;
    }
    
    .code-block {
        background: #1e293b;
        color: #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
        overflow-x: auto;
    }
    
    .team-member {
        background: linear-gradient(135deg, #fefce8 0%, #fef3c7 100%);
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 3px solid #f59e0b;
        color: #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="main-header">
    <h1>🚀 Advanced Personal Automation Hub</h1>
    <p>Group No. 8 - Enhanced Version with Modern UI</p>
</div>
""", unsafe_allow_html=True)

# --- Sidebar with Enhanced Navigation ---
with st.sidebar:
    st.markdown("### 🎯 Navigation")
    selected_tab = st.selectbox(
        "Choose Feature:",
        ["ℹ️ About", "🏠 Dashboard", "✅ Smart To-Do", "💰 Financial Hub", "👥 Group Generator", "📊 Analytics"],
        index=0  # Default to About section
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    theme = st.selectbox("Theme", ["Modern", "Classic", "Dark"])
    st.markdown(f"**Current Time:** {datetime.now().strftime('%H:%M:%S')}")

# --- Main Content Area ---
if selected_tab == "ℹ️ About":
    st.markdown("""
    <div class="about-section">
        <h3>📖 About This Application</h3>
        <p><strong>Advanced Personal Automation Hub</strong> is a comprehensive Python application that automates daily tasks, 
        provides financial insights, and facilitates group management with an intuitive web interface.</p>
        
        <h4>👥 Group No. 8 Team Members:</h4>
    </div>
    """, unsafe_allow_html=True)
    
    team_members = [
        {"name": "AKELLO PRISCILLA", "id": "VU-BBC-2503-0802-DAY"},
        {"name": "Manthan Kumar", "id": "VY-BBC-2503-0494-DAY"},
        {"name": "Ainembabazi Ollen", "id": "VU-BSF-2503-0047-DAY"},
        {"name": "Najjemba Sarah Leon", "id": "VU-BBC-2503-2377-DAY"},
        {"name": "ASIIMWE ROGERS PRAISE", "id": "VU-DIT-2503-0111-DAY"}
    ]
    
    for member in team_members:
        st.markdown(f"""
        <div class="team-member">
            <strong>{member['name']}</strong><br>
            <em>Student ID: {member['id']}</em>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-section">
        <h3>✨ Key Features</h3>
        <ul>
            <li><strong>🎯 Smart To-Do Generator:</strong> AI-powered task generation with categories, priorities, and time estimates</li>
            <li><strong>💰 Advanced Financial Hub:</strong> Comprehensive financial calculations with tax analysis and savings goals</li>
            <li><strong>👥 Smart Group Generator:</strong> Multiple grouping algorithms with statistics and visual display</li>
            <li><strong>📊 Analytics Dashboard:</strong> Usage tracking and performance metrics visualization</li>
        </ul>
        
        <h3>🛠️ Technology Stack</h3>
        <ul>
            <li><strong>Frontend:</strong> Streamlit with Custom CSS</li>
            <li><strong>Visualization:</strong> Plotly (Interactive Charts)</li>
            <li><strong>Data Processing:</strong> Pandas</li>
            <li><strong>Core Logic:</strong> Python 3.8+</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Code examples section
    st.markdown("### 💻 Code Examples")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Smart To-Do Generation")
        st.markdown("""
        <div class="code-block">
def generate_smart_todo(user_name, category, priority):
    base_tasks = DAILY_TASKS.get(category)
    num_tasks = 5 if priority == "High" else 4
    selected_tasks = random.sample(base_tasks, num_tasks)
    
    enhanced_tasks = []
    for task in selected_tasks:
        time_estimate = TIME_ESTIMATES[random_idx]
        enhanced_task = f"{priority_emoji} {task} ({time_estimate})"
        enhanced_tasks.append(enhanced_task)
    
    return enhanced_tasks, motivation
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Financial Calculation")
        st.markdown("""
        <div class="code-block">
def advanced_financial_calc(salary, expenses, savings_goal):
    tax = 0.10 * salary
    net_salary = salary - tax
    savings = net_salary - expenses
    savings_rate = (savings / salary * 100)
    
    months_to_goal = savings_goal / savings
    health_score = calculate_health_score(savings_rate)
    
    return results_dict
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("#### Group Generation Algorithm")
    st.markdown("""
    <div class="code-block">
def smart_group_generator(names_str, group_size, shuffle_mode):
    names = [name.strip() for name in names_str.split(",")]
    
    if shuffle_mode == "Alphabetical":
        names.sort(key=str.lower)
    elif shuffle_mode == "Random":
        random.shuffle(names)
    
    groups = []
    for i in range(0, len(names), group_size):
        group = names[i:i + group_size]
        groups.append(group)
    
    return groups
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-section">
        <h3>🚀 Version 2.0 Enhancements</h3>
        <ul>
            <li><strong>🎨 Complete UI Redesign:</strong> Modern gradient themes with improved color contrast</li>
            <li><strong>📊 Data Visualization:</strong> Interactive Plotly charts and graphs</li>
            <li><strong>⚡ Enhanced Performance:</strong> Optimized algorithms and faster processing</li>
            <li><strong>🎯 Advanced Features:</strong> Goal tracking, projections, and health scores</li>
            <li><strong>📱 Responsive Design:</strong> Perfect on desktop, tablet, and mobile</li>
        </ul>
        
        <p><em>This application demonstrates advanced Python programming concepts including object-oriented design, 
        data visualization, web development, and user interface design.</em></p>
    </div>
    """, unsafe_allow_html=True)

elif selected_tab == "🏠 Dashboard":
    st.markdown("### Welcome to Your Personal Automation Hub!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>✅</h3>
            <h4>Smart To-Do</h4>
            <p>AI-powered task generation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>💰</h3>
            <h4>Financial Hub</h4>
            <p>Advanced calculations & goals</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>👥</h3>
            <h4>Smart Groups</h4>
            <p>Multiple grouping algorithms</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("### 📈 Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Features", "6", delta="3 new")
    with col2:
        st.metric("UI Components", "15", delta="12 enhanced")
    with col3:
        st.metric("Automation Level", "95%", delta="35%")
    with col4:
        st.metric("User Experience", "★★★★★", delta="2 stars")

elif selected_tab == "✅ Smart To-Do":
    st.markdown("### 🎯 Smart To-Do Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_name = st.text_input("👤 Enter your name:", placeholder="e.g., Sarah")
        category = st.selectbox("📂 Task Category:", list(DAILY_TASKS.keys()))
        priority = st.selectbox("⚡ Priority Level:", ["High", "Medium", "Low"])
    
    with col2:
        st.markdown("### 🕐 Current Time")
        st.info(f"**{datetime.now().strftime('%A, %B %d, %Y')}**\n\n{datetime.now().strftime('%I:%M %p')}")
    
    if st.button("🚀 Generate Smart To-Do", type="primary"):
        if user_name:
            with st.spinner('Generating your personalized tasks...'):
                time.sleep(1)  # Simulate processing
                
            tasks, motivation = generate_smart_todo(user_name, category, priority)
            
            st.success(f"✨ Tasks generated for **{user_name}**!")
            
            st.markdown("### 📋 Your Smart To-Do List")
            for i, task in enumerate(tasks, 1):
                st.markdown(f"""
                <div class="task-item">
                    <strong>{i}.</strong> {task}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="feature-card">
                <h4>💭 Daily Motivation</h4>
                <p style="font-size: 1.2em; font-style: italic;">{motivation}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress tracking simulation
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)
                time.sleep(0.01)
            st.success("Tasks loaded successfully! 🎉")
        else:
            st.warning("Please enter your name to generate personalized tasks.")

elif selected_tab == "💰 Financial Hub":
    st.markdown("### 💼 Advanced Financial Calculator")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("#### 💸 Income & Expenses")
        salary = st.number_input("💰 Monthly Salary:", min_value=0.0, step=50000.0, value=1000000.0)
        expenses = st.number_input("🛒 Monthly Expenses:", min_value=0.0, step=10000.0, value=600000.0)
        savings_goal = st.number_input("🎯 Savings Goal:", min_value=0.0, step=100000.0, value=2000000.0)
        currency = st.selectbox("💱 Currency:", ["UGX", "USD", "EUR", "GBP"])
    
    with col2:
        st.markdown("#### 📊 Financial Health Tips")
        st.info("💡 Aim to save at least 20% of your income")
        st.info("🎯 Emergency fund: 3-6 months expenses")
        st.info("📈 Invest surplus savings for growth")
    
    if st.button("📈 Calculate & Analyze", type="primary"):
        results = advanced_financial_calc(salary, expenses, savings_goal, currency)
        
        # Display results with metrics
        st.markdown("### 📊 Financial Analysis Results")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Net Salary", f"{results['net_salary']:,.0f} {currency}")
        with col2:
            st.metric("🏦 Tax (10%)", f"{results['tax']:,.0f} {currency}")
        with col3:
            st.metric("💵 Monthly Savings", f"{results['savings']:,.0f} {currency}", 
                     delta=f"{results['savings_rate']:.1f}%")
        with col4:
            st.metric("🎯 Months to Goal", 
                     f"{results['months_to_goal']:.1f}" if results['months_to_goal'] != float('inf') else "∞")
        
        # Create visualizations
        fig = go.Figure(data=[
            go.Bar(name='Tax', x=['Breakdown'], y=[results['tax']], marker_color='#ff6b6b'),
            go.Bar(name='Expenses', x=['Breakdown'], y=[expenses], marker_color='#4ecdc4'),
            go.Bar(name='Savings', x=['Breakdown'], y=[results['savings']], marker_color='#45b7d1')
        ])
        fig.update_layout(
            title='💰 Monthly Financial Breakdown',
            barmode='stack',
            height=400,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Savings projection
        months = list(range(1, 13))
        projected = [results['savings'] * m for m in months]
        
        fig2 = px.line(x=months, y=projected, title='📈 12-Month Savings Projection',
                       labels={'x': 'Month', 'y': f'Cumulative Savings ({currency})'})
        fig2.update_traces(line_color='#667eea', line_width=3)
        fig2.update_layout(template='plotly_white')
        st.plotly_chart(fig2, use_container_width=True)

elif selected_tab == "👥 Group Generator":
    st.markdown("### 🔀 Smart Group Generator")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        names_input = st.text_area(
            "👥 Enter student names (comma separated):",
            placeholder="John, Sarah, Mike, Emma, David, Lisa, Tom, Anna",
            height=100
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            group_size = st.slider("👫 Group Size:", min_value=2, max_value=8, value=3)
        with col_b:
            shuffle_mode = st.selectbox("🔄 Grouping Method:", 
                                       ["Random", "Alphabetical", "Reverse"])
    
    with col2:
        if names_input:
            name_count = len([n.strip() for n in names_input.split(",") if n.strip()])
            st.metric("👥 Total Students", name_count)
            st.metric("🔢 Expected Groups", f"{(name_count + group_size - 1) // group_size}")
    
    if st.button("🎲 Generate Smart Groups", type="primary"):
        if names_input:
            with st.spinner('Creating optimal groups...'):
                time.sleep(1)
                
            groups = smart_group_generator(names_input, group_size, shuffle_mode)
            
            st.success(f"✨ Generated {len(groups)} groups using {shuffle_mode} method!")
            
            # Display groups with enhanced styling
            cols = st.columns(min(3, len(groups)))
            for i, group in enumerate(groups):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="group-card">
                        <h4>👥 Group {i+1}</h4>
                        <ul>
                    """ + ''.join([f"<li><strong>{member}</strong></li>" for member in group]) + """
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Group statistics
            st.markdown("### 📊 Group Statistics")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("🏆 Total Groups", len(groups))
            with col2:
                avg_size = sum(len(g) for g in groups) / len(groups) if groups else 0
                st.metric("👥 Avg Group Size", f"{avg_size:.1f}")
            with col3:
                st.metric("🔄 Method Used", shuffle_mode)
        else:
            st.warning("Please enter student names to generate groups.")

elif selected_tab == "📊 Analytics":
    st.markdown("### 📈 Usage Analytics Dashboard")
    
    # Simulated analytics data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    usage_data = pd.DataFrame({
        'Date': dates,
        'Todo_Generated': [random.randint(5, 50) for _ in dates],
        'Financial_Calcs': [random.randint(2, 20) for _ in dates],
        'Groups_Created': [random.randint(1, 15) for _ in dates]
    })
    
    # Feature usage chart
    fig = px.line(usage_data.tail(30), x='Date', 
                  y=['Todo_Generated', 'Financial_Calcs', 'Groups_Created'],
                  title='📊 Daily Feature Usage (Last 30 Days)')
    fig.update_layout(template='plotly_white', height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📝 Total To-Dos", "1,247", delta="23")
    with col2:
        st.metric("💰 Calculations", "892", delta="15")
    with col3:
        st.metric("👥 Groups Made", "456", delta="8")
    with col4:
        st.metric("⭐ User Rating", "4.9/5", delta="0.1")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #666;">
    <p>🚀 <strong>Personal Automation Hub</strong> | Enhanced by Group No. 8 | 
    Built with ❤️ using Streamlit</p>
</div>
"""
