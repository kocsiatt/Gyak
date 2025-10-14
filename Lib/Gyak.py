def name(name):

    if not name.strip():
        return "Nem adtál meg nevet"
    else:
        return "Szia, " + name




print(name(input("Kérlek add meg a neved!: ")))




