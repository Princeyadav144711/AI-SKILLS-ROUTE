from flask import Blueprint, render_template
from flask_login import login_required, current_user

from services.skill_gap_engine import calculate_skill_gap


skill_gap = Blueprint(
    "skill_gap",
    __name__
)


@skill_gap.route("/skill-gap")
@login_required
def show_skill_gap():

    career = current_user.career_goal

    if not career or career == "Not Sure":

        career = "AI/ML Engineer"

    result = calculate_skill_gap(
        current_user,
        career
    )

    return render_template(
        "skill_gap.html",
        result=result
    )