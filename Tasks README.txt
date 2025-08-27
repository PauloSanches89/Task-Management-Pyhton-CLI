---

# ✅ Task Manager – Command Line Application

This project is a Python-based task management system that allows users to register accounts, assign and manage tasks, and generate progress reports. It features user authentication, role-based permissions, text file I/O, and interactive menu navigation — all from the command line.

---

## 🧩 Problem Statement

Many small teams and individuals need a simple tool for managing personal or shared tasks, tracking progress, and organizing responsibilities. This task manager solves that problem by providing:

* Role-based user registration
* Task assignment, tracking, and updating
* Report generation for performance insights
* Persistent storage using `.txt` files

---

## 🔧 Features

### 👤 User Management

* Admin can register new users
* User login with validation
* Secure username/password matching

### 📋 Task Management

* Add new tasks
* View all tasks or only tasks assigned to the current user
* Edit or mark tasks as complete
* Restrict certain actions (like registering users) to admins

### 📊 Reports & Statistics

* Auto-generate reports:

  * Task overview
  * User-specific task stats
* Display formatted statistics directly in the terminal
* Stores data in `task_overview.txt` and `user_overview.txt`

### 📂 File-Based Storage

* User and task data stored persistently in `user.txt` and `tasks.txt`
* All reports saved for future reference

---

## 🛠 How It Works

### 1. **Login**

* Prompts for a username and password
* Validates credentials against stored data in `user.txt`

### 2. **Main Menu**

Options vary based on user role:

* Regular Users:

  * Add tasks
  * View all tasks
  * View own tasks
  * Exit
* Admin Users:

  * All above, plus:
  * Register new users
  * Generate reports
  * Display statistics

### 3. **Task Editing**

Users can:

* Reassign tasks
* Change due dates
* Mark tasks as complete
  All changes are written back to `tasks.txt`.

### 4. **Report Generation**

Admins can generate:

* 📈 `task_overview.txt`: Totals, completion status, and overdue task analysis
* 👥 `user_overview.txt`: Per-user performance breakdown with tabular formatting (using `tabulate`)

---

## 🧪 Technologies Used

* Python 3
* `datetime` for date handling
* `tabulate` for report formatting
* File I/O for persistent storage

---

## 🗂 Example Output (from `task_overview.txt`)

```
Tasks Overview
__________________________________________________

Total Number of Tasks:               8
Total Number of Completed Tasks:     5
Total Number of Incomplete tasks:    3
Total Number of Tasks Overdue:       1
Total Percentage Incomplete:         37
Total Percentage Overdue:            12
```

---

## 📁 Project Structure

```
task_manager.py          # Main application script
user.txt                 # Stores registered users and passwords
tasks.txt                # Stores task information
task_overview.txt        # Auto-generated task report
user_overview.txt        # Auto-generated user report
```

---

## 💡 Key Skills Demonstrated

* Procedural programming and modular code structure
* File reading/writing and persistent data management
* Input validation, exception handling, and logical branching
* Real-world logic implementation (e.g. deadline comparison, task stats)
* Role-based access control in CLI apps

---

## ▶️ How to Run

1. Clone the repository
2. Make sure `user.txt` and `tasks.txt` are present
3. Run the script:

```bash
python task_manager.py
```

---

## 📚 Learning Context

This project was built as part of a **Data Science Bootcamp**, emphasizing Python fundamentals, logic flow, and real-world data handling. It’s designed to demonstrate key programming skills in a structured, functional program.

---


