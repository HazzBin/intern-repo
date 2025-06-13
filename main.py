

'''
Personal Security Toolkit

Fratures:

1. Password strength checker (Finished basic implementation)
2. Check if a file is malicious using virustotal
3. Data breach checker - Haveibeenpwned API
4. Network traffic analyzer
5. Encrypted notepad

'''
import requests
import httpx
import json
import time
from colorama import Fore, Style

def main():
    print(Fore.GREEN + "="*40)
    print("Welcome to the Personal Security Toolkit!")
    print("="*40 + Style.RESET_ALL + "\n")
    print("1. Password strength checker")
    print("2. Check file safety")
    print("3. Data breach checker")
    print("4. Network traffic analyzer")
    print("5. Encrypted notepad")
    
    choice = input(Fore.GREEN + "\nPlease select a feature (1-5): " + Style.RESET_ALL)
    
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

# Checks the characteristics of the inputted password and calls to password_search function
def password_strength_checker():
    print(Fore.CYAN + "\nPassword Strength Checker" + Style.RESET_ALL)
    print("----------------------------------------------------------------------------")
    print("This tool checks the strength of your password and provides recommendations.")



    user_password = input("\nEnter a password to check its strength: ")
    recommendations = [Fore.CYAN + "\nPassword strength recommendations:\n" + Style.RESET_ALL]

    if len(user_password) < 8:
        recommendations.append("    Password is too short. It should be at least 8 characters long.")
    if not any(char.isdigit() for char in user_password):
        recommendations.append("    Password should contain at least one digit.")
    if not any(char.isupper() for char in user_password):
        recommendations.append("    Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in user_password):
        recommendations.append("    Password should contain at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in user_password):
        recommendations.append("    Password should contain at least one special character.")
       
    if len(recommendations) == 1:
        recommendations.append(Fore.GREEN + "\n  Password is strong!" + Style.RESET_ALL)
    elif len(recommendations) > 1 and len(recommendations) < 4:
        recommendations.append(Fore.YELLOW + "\n  Password is moderate. Consider implementing some of suggestions" + Style.RESET_ALL)
    elif len(recommendations) >= 4:
        recommendations.append(Fore.RED + "\n  Password is weak. Please consider changing it."  + Style.RESET_ALL)
    
    print("\n".join(recommendations) + "\n")
    password_search("10k-most-common.txt", user_password)
     
# Cross checks the user password against a file containing the 10k most commonly used passwords
def password_search(file_path, user_password):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read() 
        if user_password in content:
            print(Fore.RED + f"Dude come on. '{user_password}' is on of the top 10k most commonly used passwords. You can do better than that!" + Style.RESET_ALL)

def data_breach_checker():
    print(Fore.CYAN + "\nData Breach Checker" + Style.RESET_ALL)
    print("----------------------------------------------------------------------------")
    print("This tool checks if your email has been involved in any data breaches.")
    print("Please note that this tool uses the XposedOrNot API, which may not be available in all regions.")

    email = input("\nEnter your email: ")
    url = f"https://api.xposedornot.com/v1/check-email/{email}"  

    with httpx.Client(verify=False) as client:
        try:
            response = client.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            breaches = ", ".join(data["breaches"][0])
            email = data["email"]
            formatted_output = f"Email: {email}\nBreaches: {breaches}"
            print("\nlmao bro what is you doinnnn. You're in some data breaches bro let me get you the info...")
            for seconds in range(0,10):
                seconds += 1
                print(".")
                time.sleep(1)
                if seconds == 5:
                    print(f"I actually have the results now but im gonna make u wait a bit longer.")

            print(Fore.RED + formatted_output + Style.RESET_ALL)

            if input( Fore.CYAN + "\nWould you like to see more details? Yes[Y] / No[N]: " + Style.RESET_ALL).lower() == 'y':
                analytics_url = f"https://api.xposedornot.com/v1/breach-analytics?email={email}"
                analytic_response = client.get(analytics_url)
                analytic_response.raise_for_status()
                breach_analytic_data = analytic_response.json()

                for breach in breach_analytic_data["ExposedBreaches"]["breaches_details"]:
                    print(f"   Breach Name: {breach['breach']}")
                    print(f"   Domain: {breach['domain']}")
                    print(f"   Date: {breach['xposed_date']}")
                    print(f"   Description: {breach['details']}\n")  
                    print(f"   Amount of Records: {breach['xposed_records']}")
                    print(f"   Data Exposed: {breach['xposed_data']}")
                    print(f"   Password Risk Level: {breach['password_risk']}\n\n")

                    print("\n--------------------------------------------------------------------------\n")
            else:
                pass
        except httpx.HTTPStatusError as e:
            if not email.__contains__("@") or not email.__contains__("."):
                print("Invalid email format. Please enter a valid email address.")
                data_breach_checker()
            elif e.response.status_code == 404:
                print(f"No breaches found for {email}.")
                return
        except httpx.RequestError as e:
            print(f"Request failed: {e}")
            return

def encrypted_notepad():
    file_to_enrypt = input("Enter the file name to encrypt: ")
    key = input("Enter a key to encrypt the file: ")
    try:
        with open(file_to_enrypt, 'rb') as file:
            data = file.read()
        
        encrypted_data = ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(data.decode('utf-8')))
        
        with open(file_to_enrypt + '.enc', 'w') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        print(f"File '{file_to_enrypt}' has been encrypted and saved as '{file_to_enrypt}.enc'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_file_safety():
    pass

def network_traffic_analyzer():
    pass

# Constantly runs the main function until the user decides to exit
while True:
    main()
    
    while True:
        again = input(Fore.CYAN + "Would you like to use another tool? Yes[Y] / No[N]: " + Style.RESET_ALL).strip().lower()
        if again in ['y', 'yes']:
            break  # Move on to the next iteration
        elif again in ['n', 'no']:
            exit()  # Exit the program cleanly
        else:
            print(Fore.CYAN + "Invalid input. Please enter 'Y' or 'N'." + Style.RESET_ALL)

