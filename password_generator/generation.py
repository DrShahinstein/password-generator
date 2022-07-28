import string 
import random

def generate_password(length: int, numeric=True, lowercase=True, uppercase=True, special_chars=True) -> str:
    chars = []
    
    if lowercase:
        chars += [*string.ascii_lowercase]
    if uppercase:
        chars += [*string.ascii_uppercase]
    if numeric:
        chars += [*string.digits]
    if special_chars:
        chars += [*string.punctuation]   
        
    random.shuffle(chars)
    return "".join([chars[i] for i in range(length)])
        

