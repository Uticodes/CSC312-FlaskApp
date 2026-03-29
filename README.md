# 🌐 MIVA-CSC312 Flask Web Application

A simple and secure web application built with **Flask**, **Bootstrap 5**, and **MySQL** as part of the CSC312 Web Application Development course.


## 📋 Features

- **Homepage** — Styled landing page built with HTML and Bootstrap 5
- **Signup Page** — Form with server-side validation using `request.form`
- **MySQL Integration** — User data stored in a `tbl_user` table
- **Password Hashing** — Passwords are hashed using Werkzeug before database storage


## 🗂️ Project Structure

```
CSC312-FlaskApp/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── setup_database.sql      # MySQL table creation script
├── .env                    # Environment variables (DB credentials, secret key)
└── templates/
    ├── index.html          # Homepage
    └── signup.html         # Signup page
```


## ⚙️ Prerequisites

Make sure you have the following installed:

- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- **MySQL Server** — [mysql.com](https://dev.mysql.com/downloads/) or via XAMPP/WAMP
- **pip** (comes with Python)


## 🚀 Setup & Running the App

Follow these steps in order:

### Step 1 — Clone or Download the Project

```bash
# If using git:
git clone <repo-url>
cd CSC312-FlaskApp

# Or just unzip the downloaded folder and open a terminal inside it
```

### Step 2 — Create & Activate a Virtual Environment

```bash
# Create the virtual environment
python3 -m venv venv

# Activate it:
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up the MySQL Database

Open your MySQL client (MySQL Workbench, CLI, or phpMyAdmin) and run the SQL script:

```bash
# Using the MySQL CLI:
mysql -u root -p < setup_database.sql
```

Or manually paste the contents of `setup_database.sql` into MySQL Workbench and execute it.

This will:
1. Create the `flask_app_db` database
2. Create the `tbl_user` table with `id`, `username`, `password`, and `created_at` columns

### Step 5 — Configure Environment Variables

Open the `.env` file and update the values to match your MySQL setup. 

> [!IMPORTANT]
> **Do NOT use quotes** for your password or any other values in the `.env` file. 

**Correct:**
```env
DB_PASSWORD=mypassword123
```

**Incorrect (will cause errors):**
```env
DB_PASSWORD="mypassword123"
```

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=          # Leave blank if no password, otherwise type it directly
DB_NAME=flask_app_db
SECRET_KEY=your-secret-key-change-this-in-production
```

### Step 6 — Run the Application

```bash
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 7 — Open in Browser

Visit: **http://127.0.0.1:5000** (or **http://127.0.0.1:5001** if port 5000 is in use)


## 🧪 Testing the App

1. Go to `http://127.0.0.1:5000` — you should see the homepage.
2. Click **Sign Up** or **Get Started**.
3. Fill in a username and password.
4. Submit the form — you'll be redirected to the **new Welcome page** upon success! 🎉
5. To verify the user was saved, run this in your terminal:

```bash
mysql -u root -p -e "USE flask_app_db; SELECT id, username, created_at FROM tbl_user;"
```


## 🔐 Security Notes

- Passwords are **never stored in plain text** — they are hashed using `werkzeug.security.generate_password_hash`
- The Flask `SECRET_KEY` is loaded from the `.env` file, not hardcoded
- The `.env` file is listed in `.gitignore` to prevent credentials from being committed to version control


## 📦 Dependencies

| Package | Purpose |
|---|---|
| `flask` | Web framework |
| `mysql-connector-python` | MySQL database connection |
| `werkzeug` | Password hashing utilities |
| `python-dotenv` | Load environment variables from `.env` |


