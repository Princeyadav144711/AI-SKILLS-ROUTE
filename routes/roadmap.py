from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from extensions import db
from models.roadmap import RoadmapItem
from services.roadmap_engine import get_roadmap


roadmap = Blueprint(
    "roadmap",
    __name__
)


@roadmap.route("/roadmap")
@login_required
def show_roadmap():

    career = current_user.career_goal

    if not career or career == "Not Sure":
        career = "AI/ML Engineer"

    existing_items = RoadmapItem.query.filter_by(
        user_id=current_user.id,
        career=career
    ).order_by(
        RoadmapItem.phase
    ).all()

    if not existing_items:

        roadmap_data = get_roadmap(career)

        for item in roadmap_data:

            new_item = RoadmapItem(

                user_id=current_user.id,

                career=career,

                phase=item["phase"],

                title=item["title"],

                description=item["description"],

                skills=item["skills"],

                completed=False

            )

            db.session.add(new_item)

        db.session.commit()

        existing_items = RoadmapItem.query.filter_by(
            user_id=current_user.id,
            career=career
        ).order_by(
            RoadmapItem.phase
        ).all()

    completed = sum(
        1 for item in existing_items
        if item.completed
    )

    total = len(existing_items)

    progress = round(
        (completed / total) * 100
    ) if total else 0

    return render_template(
        "roadmap.html",
        items=existing_items,
        career=career,
        progress=progress
    )


@roadmap.route(
    "/roadmap/complete/<int:item_id>",
    methods=["POST"]
)
@login_required
def complete_item(item_id):

    item = RoadmapItem.query.filter_by(
        id=item_id,
        user_id=current_user.id
    ).first_or_404()

    item.completed = not item.completed

    db.session.commit()

    return redirect(
        url_for("roadmap.show_roadmap")
    )