def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Input weight in kilograms and height in meters
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Determine BMI category
    category = bmi_category(bmi)

    # Output the results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
