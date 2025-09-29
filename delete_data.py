import sqlite3

DB_PATH = "resume_analyzer.db"

def user_exists(user_id):
    """Check if a user exists in the users table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def delete_resumes_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM resumes WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all resumes for user_id={user_id}")

def delete_jobs_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE recruiter_id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all jobs for user_id={user_id}")

def delete_applications_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM applications
        WHERE student_id = ?
           OR job_id IN (SELECT id FROM jobs WHERE recruiter_id = ?)
    """, (user_id, user_id))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all applications related to user_id={user_id}")

def delete_analysis_logs_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM analysis_logs
        WHERE resume_id IN (SELECT id FROM resumes WHERE user_id = ?)
           OR job_id IN (SELECT id FROM jobs WHERE recruiter_id = ?)
    """, (user_id, user_id))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all analysis logs related to user_id={user_id}")

def delete_templates_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM templates WHERE uploaded_by = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all templates for user_id={user_id}")

def delete_reference_by_user_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reference WHERE uploaded_by = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted all references for user_id={user_id}")

def delete_user_by_id(user_id):
    if not user_exists(user_id):
        print(f"❌ User with user_id={user_id} does not exist.")
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted user with user_id={user_id}")

# Master function
def delete_everything_by_user_id(user_id):
    print(f"🔎 Deleting all data related to user_id={user_id} ...")
    delete_applications_by_user_id(user_id)
    delete_analysis_logs_by_user_id(user_id)
    delete_resumes_by_user_id(user_id)
    delete_jobs_by_user_id(user_id)
    delete_templates_by_user_id(user_id)
    delete_reference_by_user_id(user_id)
    delete_user_by_id(user_id)
    print("✅ All data deleted successfully for this user.")
