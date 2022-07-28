import string 
import random

def generate_password(length: int, numeric=True, lowercase=True, uppercase=True, special_chars=True) -> str:
    chars = [
        *(string.punctuation if special_chars else []),
        *(string.digits if numeric else []),
        *(string.ascii_uppercase if uppercase else []),
        *(string.ascii_lowercase if lowercase else []),
    ]
    password = ""
    for _ in range(length):
        password += random.choice(chars)

    return password
        

