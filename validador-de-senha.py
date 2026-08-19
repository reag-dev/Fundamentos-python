import json
import hmac
from hashlib import scrypt
from os import urandom

print("Validador de senha!")

filename = "stored_hashed_password.json"


def hash_password(password: str) -> str:
    salt = urandom(16)

    key = scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )

    return (salt + key).hex()


def verify_password(stored_hash: str, provided_password: str) -> bool:
    stored_hash = bytes.fromhex(stored_hash)

    salt = stored_hash[:16]
    original_key = stored_hash[16:]

    new_key = scrypt(
        provided_password.encode("utf-8"),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )

    return hmac.compare_digest(original_key, new_key)


try:
    with open(filename, "r", encoding="utf-8") as f:
        content = json.load(f)

    stored_password = content["password"]

    print("Existe uma senha cadastrada!")
    user_input = input("Informe a senha: ")

    if verify_password(stored_password, user_input):
        print("Senha validada com sucesso!")
    else:
        print("Senha incorreta!")

except FileNotFoundError:
    print("Nenhuma senha salva!")

    user_input = input("Cadastre uma senha: ")
    hashed_password = hash_password(user_input)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            {"password": hashed_password},
            f,
            indent=4
        )