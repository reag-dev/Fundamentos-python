from hashlib import scrypt, hmac
from os import urandom

print("Validador de senha!")

def hash_password(password: str) -> bytes: 
    salt = urandom(16)
    key = scrypt(
        password.encode("utf-8"),
        salt=salt
    )
    
    return salt + key

def verify_password(stored_hash: bytes, provided_password: str) -> bool: 
    salt = stored_hash[:16]
    original_key = stored_hash[16:]
    
    new_key = scrypt(
        provided_password.encode('utf-8'),
        salt=salt,
    )
    
    return hmac.compare_digest(original_key, new_key)

while True:
    password = input("Informe uma senha: ")
    hashed_password = hash_password(password)
    print(hashed_password)
    
    
    
    