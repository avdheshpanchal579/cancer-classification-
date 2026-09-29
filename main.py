"""
Cancer Classification - Python Essentials Project

Educational rule-based risk classification program.
This program is NOT a medical diagnosis tool.
"""

def get_yes_no(prompt):
    """Get a valid yes/no response from the user."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("yes", "no"):
            return value
        print("Please enter yes or no.")


def get_data():
    """Collect patient information from the command line."""
    print("\nEnter patient details")

    name = input("Name: ").strip()

    while True:
        try:
            age = int(input("Age: "))
            if age <= 0:
                print("Age must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid age.")

    while True:
        try:
            tumor = float(input("Tumor size in cm: "))
            if tumor < 0:
                print("Tumor size cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid tumor size.")

    pain = get_yes_no("Pain (yes/no): ")
    lump = get_yes_no("Lump (yes/no): ")
    weight_loss = get_yes_no("Weight loss (yes/no): ")

    return name, age, tumor, pain, lump, weight_loss


def find_result(tumor, pain, lump, weight_loss):
    """Calculate the rule-based score and classification."""
    score = 0

    if tumor > 2:
        score += 3
    elif tumor > 1:
        score += 2
    else:
        score += 1

    if pain == "yes":
        score += 1

    if lump == "yes":
        score += 2

    if weight_loss == "yes":
        score += 2

    if score >= 6:
        result = "High Risk"
    elif score >= 3:
        result = "Medium Risk"
    else:
        result = "Low Risk"

    return score, result


def show_result(name, age, tumor, score, result):
    """Display the classification result."""
    print("\n----------------------------")
    print("Cancer Classification")
    print("----------------------------")
    print("Name:", name)
    print("Age:", age)
    print("Tumor size:", tumor, "cm")
    print("Score:", score)
    print("Result:", result)
    print("----------------------------")
    print("Educational purpose only.")
    print("This result is not a medical diagnosis.")


def main():
    """Run the application."""
    print("Simple Cancer Classification")
    print("Educational purpose only")
    print("This program is not a medical diagnosis tool.")

    name, age, tumor, pain, lump, weight_loss = get_data()

    score, result = find_result(
        tumor, pain, lump, weight_loss
    )

    show_result(name, age, tumor, score, result)


if __name__ == "__main__":
    main()
