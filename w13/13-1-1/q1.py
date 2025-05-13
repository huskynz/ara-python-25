def get_demerit_points(driving_speed: float, speed_limit: int, holiday_period: bool = False) -> tuple[bool, int]:
    """
    Calculate demerit points and mandatory status for a given driving speed.
    """
    speed_difference = driving_speed - speed_limit
    
    # No penalty if not speeding
    if speed_difference <= 0:
        return (False, 0)
    
    # Determine if mandatory based on threshold
    threshold = 4 if holiday_period else 5
    mandatory = speed_difference > threshold
    
    # Calculate penalty points based on speed difference
    if speed_difference <= 10:
        return (mandatory, 10)
    elif speed_difference <= 20:
        return (True, 20)
    elif speed_difference <= 30:
        return (True, 30)
    else:
        return (True, 50)