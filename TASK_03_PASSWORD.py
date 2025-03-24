import re

def check_password_strength(password):
    """Evaluates the strength of a given password."""
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase & Lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Numbers check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special characters check
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (@, $, !, %, etc.).")

    # Determine strength level
    if strength == 4:
        return "Strong password! ✅", feedback
    elif strength == 3:
        return "Moderate password. 🔸 Try adding more complexity.", feedback
    else:
        return "Weak password! ❌ Improve the following:", feedback

# Get user input
password = input("Enter your password: ")
result, suggestions = check_password_strength(password)

# Display result
print("\n" + result)
for tip in suggestions:
    print("- " + tip)
