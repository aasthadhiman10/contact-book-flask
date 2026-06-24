# 📞 Contact Book Web Application

A lightweight, fully responsive **Contact Book Web Application** built using **Flask** for the backend, **JSON** as a lightweight file-based database, and **Bootstrap 5** for a clean, modern User Interface. This project manages contact information efficiently through full CRUD-based lifecycle routing.

---

## 🚀 Features

* **View Contacts:** Displays all saved contacts neatly in structured Bootstrap cards right on the home page.
* **Add New Contacts:** Includes an interactive web form with client-side validation to add names, emails, and phone numbers.
* **File-Based Database:** Uses a dynamic JSON storage mechanism (`contacts.json`) that saves, appends, and reads data automatically.
* **Error Resilience:** Features comprehensive `try-except` blocks to handle empty or missing data files gracefully without crashing the server.
* **Responsive UI:** Fully polished styling using modern Bootstrap 5 CDN integration.

---

## 🛠️ Tech Stack Used

* **Backend:** Python (Flask Framework)
* **Frontend:** HTML5, Jinja2 Templating Engine, Bootstrap 5 (CSS)
* **Database:** JSON (File-based local storage)

---

## 📁 Project Directory Structure

To run this app properly, your local project folder layout must be set up like this:

```text
STUDY/
│
├── app.py                  # Main Flask application logic
├── contacts.json           # Local JSON file (Database)
└── templates/              # HTML views rendered by Jinja2
    ├── index.html          # Homepage UI displaying all contacts
    └── add_contact.html    # Web form UI to add new contacts
