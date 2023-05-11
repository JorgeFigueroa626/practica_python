import re

email = "jlfigueroa626@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result= re.match(pattern,email)

if result:
    print("Es valido el correo")
else:
    print("No Es valido el correo")