def greet(raw_name: str) -> str:
    cleaned = raw_name.strip()
    if not cleaned:
        return "Nem adtál meg nevet!"
    return f"Szia, {cleaned}!"

if __name__ == "__main__":
    print(greet(input("Kérlek add meg a neved!: ")))


def check_password_strength(password: str) -> str:

    if len(password)<8:
        return "Gyenge jelszó: túl rövid."
    if not any(c.islower() for c in password):
        return "Gyenge jelszó: nincs benne kisbetű."
    if not any(c.isupper() for c in password):
        return "Gyenge jelszó: nincs nagybetű."
    if not any(c.isdigit() for c in password):
        return "Gyenge jelszó: nincs benne szám."
    return "Erős jelszó."

if __name__ == "__main__":
    print(check_password_strength(input("Kérlek add meg a jelszót!: ")))