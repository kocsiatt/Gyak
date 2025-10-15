def greet(raw_name: str) -> str:
    cleaned = raw_name.strip()
    if not cleaned:
        return "Nem adtál meg nevet!"
    return f"Szia, {cleaned}!"

if __name__ == "__main__":
    print(greet(input("Kérlek add meg a neved!: ")))




