def letter_grade(average):
    """
    Input:  average, average test scores
    Returns average letter grade
    """
    if average >= 90:
        letter = 'A'
    elif average >= 80:
        letter = 'B'
    elif average >= 70:
        letter = 'C'
    elif average >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter
