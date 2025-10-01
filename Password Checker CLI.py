import re

# Load common passwords (case-sensitive)
with open("Wordlist.txt", "r") as file:
    common_passwords = set(line.strip() for line in file)

def check_password(password):
    # Check minimum length
    if len(password) < 8:
        return "Weak: Less than 8 characters"

    # Check common passwords
    if password in common_passwords:
        return "Weak: Common password"

    # Check strength elements (optional scoring)
    score = 0
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score < 2 and len(password) < 8:
        strength = "Poor. Ensure password is greater than 12 characters or greater than 8 characters with atleast 2 complex characters."
        word_warning = ""
    elif score < 3  and len(password) < 9:
        strength = "Good. Password is up to minmum requirement but could be improved."
        word_warning = "Use 3 words to make your password greater than 12 characters"
    else:
        strength = "Strong. Password meets top requirements"
        word_warning = ""

    # Return result
    if word_warning:
        return f"{strength} {word_warning}"
    else:
        return strength

def main():
    print("=== Cyber Essentials CLI Password Checker ===")
    while True:
        password = input("Enter a password to check (or 'exit' to quit): ")
        if password.lower() == "exit":
            print("Goodbye!")
            break
        result = check_password(password)
        print(f"Password result: {result}\n")

if __name__ == "__main__":
    main()
