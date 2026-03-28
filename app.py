from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback_dev_key')  # Loaded from .env

# --- Database Configuration ---
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD') or '',
    'database': os.getenv('DB_NAME')
}

def get_db_connection():
    """Create and return a new database connection."""
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn


# --- Routes ---

@app.route('/')
def index():
    """Homepage route."""
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    """Welcome page shown after a successful signup."""
    username = request.args.get('username', 'User')
    return render_template('welcome.html', username=username)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page route - handles both displaying form and form submission."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        # --- Form Validation ---
        if not username or not password or not confirm_password:
            flash('All fields are required.', 'danger')
            return render_template('signup.html', username=username)

        if len(username) < 3:
            flash('Username must be at least 3 characters long.', 'danger')
            return render_template('signup.html', username=username)

        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('signup.html', username=username)

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('signup.html', username=username)

        # --- Password Hashing & Database Insertion ---
        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if username already exists
            cursor.execute("SELECT id FROM tbl_user WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username already taken. Please choose another.', 'danger')
                return render_template('signup.html', username=username)

            # Insert new user with hashed password
            cursor.execute(
                "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            conn.commit()
            return redirect(url_for('welcome', username=username))

        except mysql.connector.Error as e:
            flash(f'Database error: {str(e)}', 'danger')
            return render_template('signup.html', username=username)

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()   


    # GET request - just show the form
    return render_template('signup.html', username='')


if __name__ == '__main__':
    app.run(debug=True)