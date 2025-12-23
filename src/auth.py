# User Authentication Module - FIXED
def login(username, password):
    # Fixed: Added input validation
    if not username or not password:
        return False
    return authenticate_user(username, password)

def logout(user_id):
    # Logout logic
    pass

def register_user(username, email, password):
    # Registration logic
    pass
