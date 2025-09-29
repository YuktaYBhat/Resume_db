# In your main file (app.py, main.py, etc.)
from create_tables import create_database_tables, verify_tables

from insertion import *
from select_data import *
from update_data import *
from delete_data import *

# Now you can use them directly
create_database_tables()

#verify_tables()

# Change the call to insert unique data

#insert_user("shravya", "s@example.com", "sss", "student", "s S.")
#insert_resume(2, "s_Resume_v2.pdf", b'RESUME_FILE_BYTES', "Extracted summary text.")
#insert_job(2, "Software Developer", "Build web apps.", "Python, Django, SQL", 3)
# insert_application(101, 1, 5, 0.92)
# insert_template("Clean Template", "/assets/clean.pdf", 97, 3)
# insert_new_reference("Ideal Data Analyst Profile", "/ref/ideal_da.txt", "Fictional Corp", 0.95, 2)
    
#verify_tables()

#selection 

# 1. Test Login
# login_result = login_user("kavya@example.com", "secure_pass")
# #print(f"Login Result: {login_result}")

# # 2. Get Resumes
# resumes = get_user_resumes(1)
# print(f"Resumes: {resumes}")

# # 3. Get All Open Jobs
# jobs = get_all_jobs()
# #print(f"Jobs: {jobs}")

# # 4. Get User by Email
# user_data = get_user_by_email("kavya@example.com")
# #print(f"User Data: {user_data}")


# print("\n--- DEMO: Simple Explicit Update Operations ---")
#     # Example 1: Update User Role (assuming ID 1 exists)
# update_user_role(1, "admin")
        
#     # Example 2: Update Resume Final Score (assuming ID 1 exists)
# update_resume_score(1, 0.99)
    
#     # Example 3: Update Job Status (assuming ID 1 exists)
# update_job_status(1, "closed")
    
#     # Example 4: Update Application Status (assuming ID 1 exists)
# update_application_status(2, "interview")
    
#     # Example 5: Update Template ATS Score (assuming ID 1 exists)
# update_template_score(1, 0.95)

#     # Example 6: Update Reference Score (assuming ID 1 exists)
# update_reference_score(1, 0.85)  # on inserting references

#     # Example 7: Demonstrate error handling (non-existent ID)
# update_resume_score(1, 80)



# 🗑️ Delete all resumes uploaded by the user
delete_resumes_by_user_id(3)

# 🗑️ Delete all jobs posted by the user
delete_jobs_by_user_id(3)

# 🗑️ Delete all job applications submitted by or related to the user
delete_applications_by_user_id(3)

# 🗑️ Delete all analysis logs linked to that user's resumes/jobs
delete_analysis_logs_by_user_id(3)

# 🗑️ Delete all templates uploaded by that user
delete_templates_by_user_id(3)

# 🗑️ Delete all reference files uploaded by that user
delete_reference_by_user_id(3)

# 🗑️ Finally, delete the user account itself
delete_user_by_id(3)
