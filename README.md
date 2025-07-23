# Employee Management System – Desktop App (Tkinter + Python + SQLite)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)  
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Employee Management System** is a clean and intuitive desktop application built with Python's `Tkinter`, `customtkinter`, and `SQLite3`. It allows you to manage employee records – including ID, name, surname, year, and status – all through a modern, responsive UI. Ideal for small businesses, HR staff, or developers exploring GUI apps with a database backend.

---

## Preview

![App Preview](Mini-App-Employer-Management-System-with-SQLite3/Assets/preview.png)

---

## Features

- **Add New Employees**  
  Quickly add new employees with required information and status.

- **Edit & Update Records**  
  Easily update existing employee details with live field updates.

- **Delete Employees**  
  Remove employees instantly from the database.

- **SQLite3 Integration**  
  Lightweight, persistent local database with no external setup required.

- **Dark Mode GUI**  
  Built using `customtkinter` for a clean and stylish modern look.

- **Live Table View**  
  Dynamic `Treeview` showing all records in real-time with full selection support.

---

### Running the App

  Ensure you have the accompanying `database.py` file (for database logic).

  Then run the app with:

  ```bash
  python main.py
  ```

---

## How to Use

 - Start the application.  
 - Enter employee information in the input fields (ID, Name, Nachname, Jahre, Status).  
 - **"Add Employee"** to save a new record to the database.  
 - Select an employee from the table to load their info into the form.  
 - **"Update Employee"** to modify existing data.  
 - **"Delete Employee"** to remove the selected employee.  
 - **"New Employee"** to clear the form and enter fresh data.

---

## File Structure

```
.
├── main.py                 # Main GUI script
├── database.py             # Handles SQLite3 database operations
├── Assets/
│   └── e.ico               # App icon
│   └── app-preview.png     # Screenshot of the app
└── README.md               # This file
```

---

## Author

**Emin Hodžić**  
Software Engineering and Management student at TU Graz.
Experienced in web development (WordPress), image editing, and Python GUI applications.  
Created this tool as part of a self-learning journey and client-focused solutions.

For collaboration or freelance work, feel free to get in touch via [LinkedIn](https://www.linkedin.com/in/emin-hodzic) or [GitHub](https://github.com/Emin1107).

---

## License

This project is licensed under the **Apache License** – free to use, modify, and distribute.

---
