from flask import Blueprint, render_template
from flask_login import login_required, current_user

from services.resources_engine import (
    get_resources,
    get_projects
)

resources = Blueprint("resources", __name__)


@resources.route("/resources")
@login_required
def show_resources():

    career = current_user.career_goal

    if not career or career == "Not Sure":
        career = "AI/ML Engineer"

    resource_list = get_resources(career)
    project_list = get_projects(career)

    return render_template(
        "resources.html",
        career=career,
        resources=resource_list,
        projects=project_list
    )