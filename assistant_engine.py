def get_finance_response(message, profile):

    message = message.lower()

    if "50000" in message and "invest" in message:

        if profile == "Aggressive":
            return """
₹30,000 → Index Fund
₹10,000 → Flexi Cap Fund
₹5,000 → International ETF
₹5,000 → Gold ETF
"""

        elif profile == "Moderate":
            return """
₹25,000 → Index Fund
₹10,000 → Debt Fund
₹10,000 → PPF
₹5,000 → Gold ETF
"""

        else:
            return """
₹20,000 → Fixed Deposit
₹15,000 → PPF
₹10,000 → Debt Fund
₹5,000 → Gold
"""

    elif "emergency fund" in message:
        return "Maintain at least 6 months of expenses as an emergency fund."

    elif "sip" in message:
        return "SIP helps you invest a fixed amount regularly and benefit from compounding."

    elif "ppf" in message:
        return "PPF is a government-backed long-term investment option with tax benefits."

    else:
        return "Please ask about investing, SIP, PPF, emergency funds, or financial planning."