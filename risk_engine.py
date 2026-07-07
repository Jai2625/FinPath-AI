def get_risk_profile(age):

    if age < 30:
        return "Aggressive"

    elif age < 50:
        return "Moderate"

    else:
        return "Conservative"