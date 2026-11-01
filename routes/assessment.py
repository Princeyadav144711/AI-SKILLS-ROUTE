from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db


assessment = Blueprint("assessment", __name__)


@assessment.route("/assessment", methods=["GET", "POST"])
@login_required
def skill_assessment():

    if request.method == "POST":

        education = request.form.get("education")
        experience = request.form.get("experience")
        skills = request.form.get("skills")
        interests = request.form.get("interests")
        career_goal = request.form.get("career_goal")

        current_user.education = education
        current_user.experience = experience
        current_user.skills = skills
        current_user.interests = interests
        current_user.career_goal = career_goal

        db.session.commit()

        flash("Your profile has been saved successfully!")

        return redirect(url_for("dashboard"))

    return render_template("assessment.html")