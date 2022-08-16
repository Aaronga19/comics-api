from datetime import datetime, date

def age(birthdate:datetime)->int:
    """Calculates the age

    Args:
        birthdate (datetime): _description_

    Returns:
        int: _description_
    """
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age