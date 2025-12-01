def generate_wordlist(name, dob, pet, extras=[]):
    words = set()

    base_words = [name, dob, pet]
    for w in base_words:
        if w:
            words.add(w)
            words.add(w + "123")
            words.add(w + "2024")
            words.add(w[::-1])

    for extra in extras:
        words.add(extra)

    filename = "wordlist.txt"
    with open(filename, "w") as f:
        for w in words:
            f.write(w + "\n")

    print(f"Wordlist generated and saved as {filename}")
