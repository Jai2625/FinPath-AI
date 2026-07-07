import json

def get_recommendation(profile):

    with open("data/investment_rules.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get(profile, {})