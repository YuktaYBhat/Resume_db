import sqlite3
import datetime

def get_db_connection():
    """Create and return a database connection."""
    # We do not set row_factory here as these functions only execute updates.
    conn = sqlite3.connect('resume_analyzer.db')
    return conn

# ==================== SIMPLE EXPLICIT UPDATE FUNCTIONS ====================
# These functions are explicit and focus on a single, common update for the table.
# This structure is less flexible than dictionary-based updates but is more
# straightforward and avoids high-level dynamic SQL construction logic.

def update_user_role(user_id: int, new_role: str) -> bool:
    """
    Updates only the 'role' field for a specific user.
    
    Args:
        user_id (int): The ID of the user to update.
        new_role (str): The new role ('student', 'recruiter', or 'admin').
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'users' table
    sql = "UPDATE users SET role = ? WHERE id = ?"
    
    
    try:
        # Values are explicitly passed in the order they appear in the SQL query
        cursor.execute(sql, (new_role, user_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: User ID {user_id} not found.")
            return False
        print(f"Success: Updated user {user_id} role to '{new_role}'.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating user role for ID {user_id}: {e}")
        return False
    finally:
        conn.close()


def update_resume_score(resume_id: int, new_final_score: float) -> bool:
    """
    Updates only the 'final_score' field for a specific resume.
    
    Args:
        resume_id (int): The ID of the resume to update.
        new_final_score (float): The calculated final score (REAL type).
        
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'resumes' table
    sql = "UPDATE resumes SET final_score = ? WHERE id = ?"
    
    try:
        # Values are explicitly passed in order (new_final_score, resume_id)
        cursor.execute(sql, (new_final_score, resume_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: Resume ID {resume_id} not found.")
            return False
        print(f"Success: Updated resume {resume_id} final score to {new_final_score}.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating resume score for ID {resume_id}: {e}")
        return False
    finally:
        conn.close()


def update_job_status(job_id: int, new_status: str) -> bool:
    """
    Updates only the 'status' field for a specific job.
    
    Args:
        job_id (int): The ID of the job posting to update.
        new_status (str): The new status (e.g., 'open', 'closed', 'paused').
        
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'jobs' table
    sql = "UPDATE jobs SET status = ? WHERE id = ?"
    
    try:
        cursor.execute(sql, (new_status, job_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: Job ID {job_id} not found.")
            return False
        print(f"Success: Updated job {job_id} status to '{new_status}'.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating job status for ID {job_id}: {e}")
        return False
    finally:
        conn.close()


def update_application_status(application_id: int, new_status: str) -> bool:
    """
    Updates only the 'status' field for a specific application.
    
    Args:
        application_id (int): The ID of the application record to update.
        new_status (str): The new status (e.g., 'submitted', 'reviewed', 'rejected', 'interview').
        
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'applications' table
    sql = "UPDATE applications SET status = ? WHERE id = ?"
    
    try:
        cursor.execute(sql, (new_status, application_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: Application ID {application_id} not found.")
            return False
        print(f"Success: Updated application {application_id} status to '{new_status}'.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating application status for ID {application_id}: {e}")
        return False
    finally:
        conn.close()


def update_template_score(template_id: int, new_ats_score: float) -> bool:
    """
    Updates only the 'ats_score' field for a specific resume template.
    
    Args:
        template_id (int): The ID of the template to update.
        new_ats_score (float): The updated ATS compliance score (REAL type).
        
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'templates' table
    sql = "UPDATE templates SET ats_score = ? WHERE id = ?"
    
    try:
        cursor.execute(sql, (new_ats_score, template_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: Template ID {template_id} not found.")
            return False
        print(f"Success: Updated template {template_id} ATS score to {new_ats_score}.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating template score for ID {template_id}: {e}")
        return False
    finally:
        conn.close()


def update_reference_score(reference_id: int, new_score: float) -> bool:
    """
    Updates only the 'score' field for a specific reference document.
    
    Args:
        reference_id (int): The ID of the reference document to update.
        new_score (float): The updated benchmark score (REAL type).
        
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple, explicit SQL query string for the 'reference' table
    sql = "UPDATE reference SET score = ? WHERE id = ?"
    
    try:
        cursor.execute(sql, (new_score, reference_id))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Info: Reference ID {reference_id} not found.")
            return False
        print(f"Success: Updated reference {reference_id} score to {new_score}.")
        return True
    except sqlite3.Error as e:
        print(f"Database error updating reference score for ID {reference_id}: {e}")
        return False
    finally:
        conn.close()

# The exported public interface for this module
__all__ = [
    'update_user_role',
    'update_resume_score',
    'update_job_status',
    'update_application_status',
    'update_template_score',
    'update_reference_score'
]
