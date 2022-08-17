from datetime import datetime, date

def age(birthdate:datetime)->int:
    """Calculates the age.

    Args:
        birthdate (datetime): Data of birth of the user.

    Returns:
        int: Actual age.
    """
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age