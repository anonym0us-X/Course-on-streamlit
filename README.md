# Streamlit To-Do List App

This is a simple and visually appealing To-Do List application built using **Streamlit**.  
The app demonstrates core Streamlit concepts including page setup, widgets, sidebar, and state management.

---

## Features

- **Page Setup:** Custom page title and icon using `st.set_page_config`.
- **Task Input:** Text input box to add new tasks.
- **Priority Selector:** Dropdown menu to assign priority levels (High, Medium, Low) with colored badges.
- **Task List:**  
  - Displays tasks with checkboxes to mark completion.  
  - Delete button to remove tasks.  
  - Completed tasks are shown with strikethrough styling.
- **Statistics:**  
  - Shows total tasks, completed tasks, and completion rate with a progress bar.  
  - Stats are displayed in visually distinct sections.
- **Sidebar:**  
  - Priority filter to view tasks by priority.  
  - Button to clear all completed tasks.

---

## How to Run

1. Clone this repository:
  git clone <your-repo-url>,
  cd <your-repo-folder>


2. Install dependencies:
  pip install streamlit

3. Run the app:
   streamlit run filename.py


---

## Learnings from the Streamlit Course

- Understanding Streamlit’s layout primitives: `st.container()`, `st.columns()`, `st.sidebar`.
- Managing app state with `st.session_state`.
- Styling with Markdown and inline HTML for better UI.
- Handling user inputs and events with forms, buttons, and checkboxes.
- Creating responsive and user-friendly interfaces.

---

## Future Improvements

- Add user authentication.
- Save tasks persistently (e.g., using a database or file).
- Add task deadlines and reminders.
- Enhance UI with custom components or themes.

---

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)

---

Feel free to contribute or raise issues!

---

*Developed as part of a Streamlit learning course.*
