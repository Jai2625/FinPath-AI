import math


def financial_health_score(income, expenses, savings):

    score = 0

    savings_rate = ((income - expenses) / income) * 100

    if savings_rate >= 30:
        score += 40

    emergency_fund_required = expenses * 6

    if savings >= emergency_fund_required:
        score += 30

    if savings > 50000:
        score += 30

    return score


def calculate_sip(goal_amount, years):

    annual_return = 0.12

    monthly_rate = annual_return / 12

    months = years * 12

    sip = goal_amount * monthly_rate / (
        ((1 + monthly_rate) ** months) - 1
    )

    return round(sip, 2)
def emergency_fund_status(expenses, savings):

    required_fund = expenses * 6

    if savings >= required_fund:
        status = "Healthy"
    else:
        status = "Needs Improvement"

    return required_fund, status

def get_health_rating(score):

    if score >= 90:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Needs Improvement"
    
def emergency_fund_status(expenses, savings):

    required_fund = expenses * 6

    if savings >= required_fund:
        status = "Healthy ✅"
    else:
        status = "Needs Improvement ⚠️"

    return required_fund, status