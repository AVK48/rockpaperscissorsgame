#importing the getpass module
import getpass
import string
#defining the function password
def password(p):
    if len(p)< 8:
        return"Invalid: must  be at least 8 character long"
    has_uppercase = any(ch.isupper() for ch in p)
    has_lowercase = any(ch.islower() for ch in p)
    has_digit = any(ch.isdigit() for ch in p)
    has_special = any(ch in string.punctuation for ch in p)  


    if has_uppercase and has_lowercase and has_digit and has_special:
        return "Strong password"
    else:
        return "Invalid: must contain atleast one captial letter, small letter,sepcial character, and a digit"
    
user_input= getpass.getpass("Enter the password:")
print(password(user_input))
