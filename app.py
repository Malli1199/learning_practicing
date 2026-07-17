# app.py
import streamlit as st

# Set up page configurations
st.set_page_config(page_title="Secure Login Portal", page_icon="🔒", layout="centered")

# Initialize session states so Streamlit remembers if a user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Dummy database of valid users (In a real app, this would check a secure database!)
USER_DATABASE = {
    "admin": "SecurePassword123",
    "developer": "DevOpsPass2026"
}

def login_user(username, password):
    """Validates the input credentials against our database."""
    if username in USER_DATABASE:
        if USER_DATABASE[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome back, {username}! Logging you in...")
            st.rerun() # Refresh the page to show the dashboard
        else:
            st.error("Incorrect password. Please try again.")
    else:
        st.error("Username not found.")

def logout_user():
    """Clears the session and logs the user out."""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# --- Page Routing Logic ---

if not st.session_state.logged_in:
    # 1. Show the Login Page UI if user is not authenticated
    st.title("🔒 Security Portal")
    st.subheader("Please sign in to access your environment.")
    
    # Create a clean login form container
    with st.form("login_form"):
        username_input = st.text_input("Username", placeholder="Enter your username")
        password_input = st.text_input("Password", type="password", placeholder="Enter your password")
        
        submit_button = st.form_submit_button("Sign In")
        
        if submit_button:
            if username_input and password_input:
                login_user(username_input, password_input)
            else:
                st.warning("Please fill out both fields!")

else:
    # 2. Show the Secured Dashboard if user is logged in
    st.title("🚀 Developer Dashboard")
    st.write(f"Logged in securely as: **{st.session_state.username}**")
    st.divider()
    
    st.success("Access Granted! You have successfully bypassed the secure login gateway.")
    
    st.info("""
    **Next Pipeline Steps to complete:**
    * [x] Build Docker Container
    * [ ] Push Image to Hub
    * [ ] Continuous Deployment Check
    """)
    
    # Logout option
    if st.button("Log Out"):
        logout_user()