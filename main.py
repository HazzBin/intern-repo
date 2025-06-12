

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
    
    print("\n".join(recommendations) + "\n")
    password_search("10k-most-common.txt", user_password)
     

def password_search(file_path, user_password):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read() 
        if user_password in content:
            print(f"'{user_password}' is one of the top 10k most commonly used passwords in the world. Change your password immediately!")



        
while True:
    main()
    again = input("Would you like to use another tool? Yes[Y] / No[N]: ")
    if again.lower() == "no" or again.lower() == "n":
        break