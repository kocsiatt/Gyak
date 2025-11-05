import re


def check_password_with_regex(password: str) -> str:
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$"

    if re.fullmatch(pattern, password):
        return "Erős jelszó."
    else:
        return "Gyenge jelszó."

print(check_password_with_regex("Aaaaaaaa@"))