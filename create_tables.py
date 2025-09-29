import sqlite3

def create_database_tables():
    """Create all tables for Resume Analyzer application"""
    conn = sqlite3.connect('resume_analyzer.db')
    cursor = conn.cursor()
    
    # 1. users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT CHECK (role IN ('student', 'recruiter', 'admin')),
        full_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )
    ''')
    
    # 2. resumes table (with uploaded_file column)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        file_path TEXT,
        uploaded_file BLOB,  -- Store actual file data
        extracted_text TEXT,
        ats_score REAL,
        skill_match_pct REAL,
        similarity_score REAL,
        final_score REAL,
        upload_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    ''')
    
    # 3. jobs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recruiter_id INTEGER,
        title TEXT,
        job_description TEXT,
        required_skills TEXT,
        min_experience INTEGER,
        posted_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'open',
        FOREIGN KEY (recruiter_id) REFERENCES users (id) ON DELETE CASCADE
    )
    ''')
    
    # 4. applications table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        student_id INTEGER,
        resume_id INTEGER,
        similarity_score REAL,
        status TEXT DEFAULT 'submitted',
        applied_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE CASCADE,
        FOREIGN KEY (student_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (resume_id) REFERENCES resumes (id) ON DELETE CASCADE
    )
    ''')
    
    # 5. templates table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS templates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        file_path TEXT,
        ats_score REAL,
        uploaded_by INTEGER,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (uploaded_by) REFERENCES users (id) ON DELETE SET NULL
    )
    ''')
    
    # 6. reference table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reference (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        file_path TEXT,
        company TEXT,
        score REAL,
        uploaded_by INTEGER,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (uploaded_by) REFERENCES users (id) ON DELETE SET NULL
    )
    ''')
    
    # 7. analysis_logs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analysis_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_id INTEGER,
        job_id INTEGER,
        analysis_results TEXT,  -- JSON dump of analysis
        analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (resume_id) REFERENCES resumes (id) ON DELETE CASCADE,
        FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE SET NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ All tables created successfully!")

def verify_tables():
    """Verify that all tables were created correctly"""
    conn = sqlite3.connect('resume_analyzer.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("\n📋 Tables in database:")
    expected_tables = ['users', 'resumes', 'jobs', 'applications', 'templates', 'reference', 'analysis_logs']
    
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        status = "✅" if table_name in expected_tables else "❌"
        print(f"  {status} {table_name}: {count} records")
    
    # Check if all expected tables exist
    created_tables = [table[0] for table in tables]
    missing_tables = set(expected_tables) - set(created_tables)
    
    if missing_tables:
        print(f"\n❌ Missing tables: {missing_tables}")
    else:
        print(f"\n✅ All {len(expected_tables)} tables created successfully!")
    
    conn.close()
__all__ = [
    'create_database_tables',
    'verify_tables',
    'initialize_database',
    'get_db_connection'
]
