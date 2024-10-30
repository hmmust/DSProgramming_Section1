import sys

def email_validator(func1):
    def wrapper(useremail, message):
        if len(useremail.split("@")) >1:
            return func1(useremail,message)
        else:
            print("Email is invalid")
            return    
    return wrapper

@email_validator
def send_email(e,m):
    print(f'sending email to :{e}:{m}')

@email_validator

def send_message(e,m):
    print(f'sending message to :{e}:{m}')

email = sys.argv[1]
message = sys.argv[2]

send_email(email,message)
send_message(email,message)




