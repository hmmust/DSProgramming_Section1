import sys,os
from dotenv import load_dotenv

load_dotenv()

email = sys.argv[1]
message = sys.argv[2]

print(f'sending email to :{email}:{message}')

username = os.getenv("NAME")
password = os.getenv("PASSWORD")
java = os.getenv("JAVA_HOME")

print(username,password,java)

