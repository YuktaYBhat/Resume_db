# select_operations.py

import sqlite3
import hashlib

# NOTE: We can import get_db_connection from insert_operations, but it's often 
# simpler for small projects to keep utility functions defined in both files 
# if they are logically separate modules.
def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect('resume_analyzer.db')
    conn.row_factory = sqlite3.Row
    return conn

# ==================== SELECT OPERATIONS (GET DATA) ====================

def login_user(email, password):
    """Login user by verifying credentials"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hash the provided password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # SELECT operation
    cursor.execute('SELECT * FROM users WHERE email = ? AND password_hash = ?', 
                    (email, password_hash))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"success": True, "user": dict(user)}
    else:
        return {"success": False, "message": "Invalid email or password"}

def get_user_resumes(user_id):
    """Get all resumes for a specific user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SELECT operation
    cursor.execute('SELECT * FROM resumes WHERE user_id = ? ORDER BY upload_at DESC', (user_id,))
    resumes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resumes

def get_all_jobs():
    """Get all available jobs"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SELECT operation
    cursor.execute('SELECT * FROM jobs WHERE status = "open" ORDER BY posted_on DESC')
    jobs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jobs

def get_user_by_email(email):
    """Get user by email"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # SELECT operation
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

__all__ = [
    'get_db_connection', # Included for utility
    'login_user', 
    'get_user_resumes',
    'get_all_jobs',
    'get_user_by_email'
]