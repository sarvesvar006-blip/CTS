def login_system(user, pwd):
    
    if not user.strip() or not pwd.strip():
        return "Invalid input! Username and password cannot be empty."

   
    if user == "admin":
        if pwd == "pass123":
            return "Login Successful"
        else:
            return "Incorrect Password"
    else:
        return "Invalid Username"



user = "admin"
pwd = "pass123"

result = login_system(user, pwd)
print(f"Status: {result}")