# insert_operations.py

import sqlite3
import hashlib

# Database connection function (Necessary for all operations)
def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect('resume_analyzer.db')
    conn.row_factory = sqlite3.Row
    return conn

# ==================== INSERT OPERATIONS ====================

def insert_user(username, email, password, role, full_name):
    """Insert a new user into users table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute('''
        INSERT INTO users (username, email, password_hash, role, full_name)
        VALUES (?, ?, ?, ?, ?)
        ''', (username, email, password_hash, role, full_name))
        
        conn.commit()
        user_id = cursor.lastrowid
        return {"success": True, "user_id": user_id, "message": "User registered successfully!"}
    except sqlite3.IntegrityError:
        return {"success": False, "message": "Username or email already exists!"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    finally:
        conn.close()

def insert_resume(user_id, filename, file_data, extracted_text=""):
    """Insert a resume into resumes table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO resumes (user_id, filename, uploaded_file, extracted_text)
        VALUES (?, ?, ?, ?)
        ''', (user_id, filename, file_data, extracted_text))
        
        conn.commit()
        resume_id = cursor.lastrowid
        return {"success": True, "resume_id": resume_id, "message": "Resume uploaded successfully!"}
    except Exception as e:
        return {"success": False, "message": f"Error uploading resume: {str(e)}"}
    finally:
        conn.close()

def insert_job(recruiter_id, title, job_description, required_skills, min_experience=0):
    """Insert a job posting into jobs table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO jobs (recruiter_id, title, job_description, required_skills, min_experience)
        VALUES (?, ?, ?, ?, ?)
        ''', (recruiter_id, title, job_description, required_skills, min_experience))
        
        conn.commit()
        job_id = cursor.lastrowid
        return {"success": True, "job_id": job_id, "message": "Job created successfully!"}
    except Exception as e:
        return {"success": False, "message": f"Error creating job: {str(e)}"}
    finally:
        conn.close()

def insert_application(job_id, student_id, resume_id, similarity_score=0.0):
    """Insert a job application into applications table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO applications (job_id, student_id, resume_id, similarity_score)
        VALUES (?, ?, ?, ?)
        ''', (job_id, student_id, resume_id, similarity_score))
        
        conn.commit()
        application_id = cursor.lastrowid
        return {"success": True, "application_id": application_id, "message": "Application submitted successfully!"}
    except Exception as e:
        return {"success": False, "message": f"Error submitting application: {str(e)}"}
    finally:
        conn.close()

def insert_template(title, file_path, ats_score, uploaded_by):
    """Insert a resume template into templates table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO templates (title, file_path, ats_score, uploaded_by)
        VALUES (?, ?, ?, ?)
        ''', (title, file_path, ats_score, uploaded_by))
        
        conn.commit()
        template_id = cursor.lastrowid
        return {"success": True, "template_id": template_id, "message": "Template added successfully!"}
    except Exception as e:
        return {"success": False, "message": f"Error adding template: {str(e)}"}
    finally:
        conn.close()


def insert_new_reference(title: str, file_path: str, company: str, score: float, uploaded_by_id: int) -> int | None:
    """Inserts a new reference document record and returns the new reference's ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = """
    INSERT INTO reference (title, file_path, company, score, uploaded_by) 
    VALUES (?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(sql, (title, file_path, company, score, uploaded_by_id))
        conn.commit()
        print(f"Success: Added new reference document '{title}'.")
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error inserting reference: {e}")
        return None
    finally:
        conn.close()


__all__ = [
    'get_db_connection', # Included for utility
    'insert_user',
    'insert_resume',
    'insert_job', 
    'insert_application',
    'insert_template',
    'insert_new_reference'
]