import bisect

# BMI thresholds and corresponding categories
bmi_categories = {
    0: "Underweight",
    18.5: "Normal weight",
    25.0: "Overweight",
    30.0: "Obesity Class I",
    35.0: "Obesity Class II",
    40.0: "Obesity Class III",
}

bmi_brackets = list(bmi_categories.keys())
bmi_labels = list(bmi_categories.values())


def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height**2)


def classify_bmi(bmi: float) -> str:
    if bmi < 0:
        return "Invalid BMI"

    index = bisect.bisect_right(bmi_brackets, bmi) - 1
    return bmi_labels[index] if index < len(bmi_labels) else "Unknown"


def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        height = float(input("Enter your height in meters: "))
        if height <= 0:
            raise ValueError("Height must be a positive number.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"BMI: {bmi:.2f}, Category: {category}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers for weight and height.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
