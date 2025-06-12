

'''
Personal Security Toolkit

Fratures:

1. Password strength checker
2. Check if a file is malicious using virustotal
3. Data breach checker - Haveibeenpwned API
4. Network traffic analyzer
5. Encrypted notepad

'''
import zipfile

def main():
    print("Welcome to the Personal Security Toolkit!\n")
    print("1. Password strength checker")
    print("2. Check file safety")
    print("3. Data breach checker")
    print("4. Network traffic analyzer")
    print("5. Encrypted notepad")
    
    choice = input("Please select a feature (1-5): ")
    
    if choice == '1':
        password_strength_checker()
    elif choice == '2':
        check_file_safety()
    elif choice == '3':
        data_breach_checker()
    elif choice == '4':
        network_traffic_analyzer()
    elif choice == '5':
        encrypted_notepad()
    else:
        print("Invalid choice, please try again.")

def password_strength_checker():
    user_password = input("Enter a password to check its strength: ")
    recommendations = ["Password strength recommendations:"]

    if len(user_password) < 8:
        recommendations.append("Password is too short. It should be at least 8 characters long.")
    if not any(char.isdigit() for char in user_password):
        recommendations.append("Password should contain at least one digit.")
    if not any(char.isupper() for char in user_password):
        recommendations.append("Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in user_password):
        recommendations.append("Password should contain at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in user_password):
        recommendations.append("Password should contain at least one special character.")
       
    if len(recommendations) == 1:
        recommendations.append("Password is strong!")
    elif len(recommendations) > 1 and len(recommendations) < 4:
        recommendations.append("Password is moderate. Consider implementing some of suggestions")
    elif len(recommendations) >= 4:
        recommendations.append("Password is weak. Please consider changing it.")

    check_password_in_zip("rockyou.txt.zip", user_password)

    return print("\n".join(recommendations) + "\n")

def check_password_in_zip(zip_path, user_password):
    with zipfile.ZipFile(zip_path, 'r') as z:
        file_name = z.namelist()[0]  # Get the first (and only) file inside the ZIP
        
        with z.open(file_name) as f:
            content = f.read().decode('utf-8')  # Read and decode the text file
            
            if user_password in content:
                return f"Password found in '{file_name}'!"
            else:
                return "Password NOT found in the file."


        
while True:
    main()
    
