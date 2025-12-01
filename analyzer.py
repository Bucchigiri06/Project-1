import re

def analyze_password(password):
    score = 0
    remarks = ""

    # Score 1 - Length requirement
    if len(password) >= 8:
        score += 1
    else:
        remarks += "- Use at least 8 characters\n"

    # Score 2 - Lowercase
    if re.search("[a-z]", password):
        score += 1
    else:
        remarks += "- Add lowercase letters\n"

    # Score 3 - Uppercase
    if re.search("[A-Z]", password):
        score += 1
    else:
        remarks += "- Add uppercase letters\n"

    # Score 4 - Numbers
    if re.search("[0-9]", password):
        score += 1
    else:
        remarks += "- Add numeric digits\n"

    # Score 5 - Special characters
    if re.search("[@#$%^&*()!_+=<>?/{}|~-]", password):
        score += 1
    else:
        remarks += "- Add special characters (@, #, $, %, &, *)\n"

    # Score 6 - Strong length
    if len(password) >= 12:
        score += 1

    print("\n--- PASSWORD STRENGTH REPORT ---")
    print(f"Password entered: {password}")
    print(f"Strength Score: {score} / 6")

    if score <= 2:
        print("Strength: VERY WEAK ❌")
    elif score <= 4:
        print("Strength: MODERATE ⚠️")
    else:
        print("Strength: STRONG ✅")

    if remarks:
        print("\nSuggestions to improve:")
        print(remarks)

    print("---------------------------------\n")

    return score
