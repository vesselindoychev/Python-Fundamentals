def grades(grade):
    if 2.00 <= grade < 3.00:
        return "Fail"

    elif grade < 3.5:
        return "Poor"

    elif grade < 4.5:
        return "Good"

    elif grade < 5.5:
        return "Very Good"

    elif grade <= 6.0:
        return "Excellent"


grade = float(input())
print(grades(grade))
