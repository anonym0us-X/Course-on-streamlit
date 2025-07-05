import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="📝")

st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0;'>📝 To-Do List</h1>
    <hr style="margin-top: 0;">
    """,
    unsafe_allow_html=True,
)

# Sidebar for filters and actions
st.sidebar.header("Options")
filter_priority = st.sidebar.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])
clear_completed = st.sidebar.button("Clear Completed Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Add Task Section ---
with st.container():
    st.markdown(
        """
        <div style="background-color:#f6f9fc; padding: 24px 24px 10px 24px; border-radius: 14px; margin-bottom: 18px;">
        <h3 style="margin-bottom: 12px;">➕ Add a New Task</h3>
        """,
        unsafe_allow_html=True,
    )
    with st.form("Add Task", clear_on_submit=True):
        task_name = st.text_input("Task description", key="task_input")
        priority = st.selectbox("Select priority", ["High 🔴", "Medium 🟠", "Low 🟢"], key="priority_input")
        submitted = st.form_submit_button("Add Task")
        if submitted and task_name.strip():
            st.session_state.tasks.append({
                "task": task_name.strip(),
                "priority": priority,
                "completed": False
            })
    st.markdown("</div>", unsafe_allow_html=True)

# --- Stats Section ---
total_tasks = len(st.session_state.tasks)
completed_tasks = sum(task["completed"] for task in st.session_state.tasks)
completion_ratio = (completed_tasks / total_tasks) if total_tasks > 0 else 0.0

with st.container():
    st.markdown(
        """
        <div style="background-color:#fffbe6; padding: 24px; border-radius: 14px; margin-bottom: 18px;">
        <h3>📊 Stats</h3>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div style="display: flex; gap: 32px; margin-bottom: 8px;">
            <div style="flex: 1; background: #f0f2f6; border-radius: 10px; padding: 16px; text-align: center;">
                <span style="font-size:18px;">📝 Total Tasks</span><br>
                <span style="font-size:32px; font-weight:bold;">{total_tasks}</span>
            </div>
            <div style="flex: 1; background: #e6f9f0; border-radius: 10px; padding: 16px; text-align: center;">
                <span style="font-size:18px;">✅ Completed</span><br>
                <span style="font-size:32px; font-weight:bold;">{completed_tasks}</span>
            </div>
            <div style="flex: 1; background: #f9f6e6; border-radius: 10px; padding: 16px; text-align: center;">
                <span style="font-size:18px;">📈 Completion Rate</span><br>
                <span style="font-size:32px; font-weight:bold;">{completion_ratio*100:.1f}%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(completion_ratio)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Task List Section ---
with st.container():
    st.markdown(
        """
        <div style="background-color:#f6f9fc; padding: 24px; border-radius: 14px;">
        <h3 style="margin-bottom: 30px;">📋 Task List</h3>
        """,
        unsafe_allow_html=True,
    )
    if total_tasks == 0:
        st.info("No tasks yet. Add your first task above!")
    else:
        delete_indices = []
        for i, task in enumerate(st.session_state.tasks):
            if filter_priority != "All" and not task["priority"].startswith(filter_priority):
                continue

            priority_color = {
                "High 🔴": "#ff4b4b",
                "Medium 🟠": "#ffb347",
                "Low 🟢": "#4caf50"
            }[task["priority"]]

            task_html = (
                f'<span style="text-decoration: line-through; color: gray;">{task["task"]}</span>'
                if task["completed"]
                else f'<span style="font-weight: 600;">{task["task"]}</span>'
            )

            # Use columns for layout with extra bottom margin for spacing
            tcol1, tcol2, tcol3, tcol4 = st.columns([0.06, 0.68, 0.16, 0.10])
            # Wrap the entire row in a container with bottom margin
            with st.container():
                st.markdown(
                    """
                    <style>
                    .task-row {
                        margin-bottom: 22px;  /* Space between tasks */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown('<div class="task-row">', unsafe_allow_html=True)
                with tcol1:
                    completed = st.checkbox("", value=task["completed"], key=f"complete_{i}")
                    if completed != task["completed"]:
                        st.session_state.tasks[i]["completed"] = completed

                with tcol2:
                    st.markdown(task_html, unsafe_allow_html=True)

                with tcol3:
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; height: 100%;">
                            <span style="background-color: {priority_color}; color: white; padding: 6px 14px; border-radius: 10px; font-size: 15px; display: inline-block;">
                                {task["priority"]}
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with tcol4:
                    if st.button("🗑️", key=f"delete_{i}"):
                        delete_indices.append(i)
                st.markdown('</div>', unsafe_allow_html=True)

        for idx in sorted(delete_indices, reverse=True):
            st.session_state.tasks.pop(idx)
            st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
