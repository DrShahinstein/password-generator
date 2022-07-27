import string 
import random

specials = "!@#$%^&*()"

def generate_password(length: int, alphabetic=True, numeric=True, lowercase=True, uppercase=True, special_chars=True) -> str:
    chars = []
    if alphabetic:
        if lowercase:
            chars += [*string.ascii_lowercase]
        if uppercase:
            chars += [*string.ascii_uppercase]
    if numeric:
        chars += [*string.digits]
    if special_chars:
        chars += [*specials]   
    random.shuffle(chars)
    
    return "".join([chars[i] for i in range(length)])
        

