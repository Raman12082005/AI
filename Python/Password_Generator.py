import random
import string

def generate_password(length):
    character = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    
    password = []

    for i in range(length):
        password.append(random.choice(character))

    random.shuffle(password)
    password = "".join(password)

    return password

length = int(input("Enter length of Password: "))
print("The Generated password is : ",generate_password(length))


