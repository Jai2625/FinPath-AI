from flask import Flask, render_template, request

from recommendation_engine import get_recommendation

from finance_engine import (
    financial_health_score,
    calculate_sip,
    get_health_rating,
    emergency_fund_status
)

from chart_generator import create_pie_chart
from assistant_engine import get_finance_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    age = int(request.form["age"])

    risk_preference = request.form["risk_preference"]

    income = float(request.form["income"])
    expenses = float(request.form["expenses"])
    savings = float(request.form["savings"])

    goal_amount = float(request.form["goal_amount"])
    goal_years = int(request.form["goal_years"])

    profile = risk_preference

    recommendations = get_recommendation(profile)

    create_pie_chart(recommendations)

    score = financial_health_score(
        income,
        expenses,
        savings
    )

    health_rating = get_health_rating(score)

    required_fund, fund_status = emergency_fund_status(
        expenses,
        savings
    )

    required_sip = calculate_sip(
        goal_amount,
        goal_years
    )

    return render_template(
        "result.html",
        profile=profile,
        recommendations=recommendations,
        score=score,
        health_rating=health_rating,
        required_sip=required_sip,
        goal_amount=goal_amount,
        goal_years=goal_years,
        required_fund=required_fund,
        fund_status=fund_status,
        savings=savings
    )


@app.route("/assistant", methods=["GET", "POST"])
def assistant():

    response = ""

    if request.method == "POST":

        profile = request.form["profile"]
        message = request.form["message"]

        response = get_finance_response(
            message,
            profile
        )

    return render_template(
        "assistant.html",
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)