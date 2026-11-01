from flask import Blueprint, render_template
from flask_login import login_required, current_user

from extensions import db
from models.recommendation import Recommendation
from services.recommendation_engine import calculate_recommendations


recommendation = Blueprint(
    "recommendation",
    __name__
)


@recommendation.route("/recommendation")
@login_required
def show_recommendation():

    results = calculate_recommendations(
        current_user
    )

    # Remove previous recommendations
    Recommendation.query.filter_by(
        user_id=current_user.id
    ).delete()

    # Save new recommendations
    for result in results:

        new_recommendation = Recommendation(

            user_id=current_user.id,

            career=result["career"],

            score=result["score"],

            reason=result["reason"]

        )

        db.session.add(new_recommendation)

    db.session.commit()

    return render_template(
        "recommendation.html",
        recommendations=results
    )