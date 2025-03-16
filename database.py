  GNU nano 8.3                          database.py
import sqlite3
from datetime import datetime, timedelta

DB_PATH = "database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        trials_left INTEGER DEFAULT 5,
                        subscription_end DATE,
                        referrals INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                        user_id INTEGER,
                        amount REAL,
                        payment_method TEXT,
                        date TEXT)''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def log_payment(user_id, amount, method):                                                   conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (user_id, amount, payment_method, date) VALUES>
                   (user_id, amount, method, datetime.now().strftime("%Y-%m-%d %H:%M:%S>
    conn.commit()
    conn.close()
