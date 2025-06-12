

'''
Personal Security Toolkit

Fratures:

1. Password strength checker
2. Check if a file is malicious using virustotal
3. Data breach checker
4. Network traffic analyzer
5. Encrypted notepad

'''

def main():
    print("Welcome to the Personal Security Toolkit!")
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


d