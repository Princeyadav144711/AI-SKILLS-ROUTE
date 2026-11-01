from flask import Blueprint, render_template
from flask_login import login_required, current_user

from services.career_advisor import generate_career_advice


career_advisor = Blueprint("career_advisor", __name__)


@career_advisor.route("/career-advisor")
@login_required
def show_career_advisor():

    advice = generate_career_advice(current_user)

    return render_template(
        "career_advisor.html",
        advice=advice
    )