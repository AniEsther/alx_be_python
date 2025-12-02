
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float (this is where ValueError can occur)
        numerator = float(numerator)
        denominator = float(denominator)

        return numerator / denominator

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only"