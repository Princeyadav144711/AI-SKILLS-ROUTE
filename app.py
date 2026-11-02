from models.recommendation import Recommendation
from models.roadmap import RoadmapItem

from services.recommendation_engine import calculate_recommendations
from services.skill_gap_engine import calculate_skill_gap
from services.resources_engine import get_resources, get_projects

from flask import Flask, render_template
from flask_login import login_required, current_user

from config import Config
from extensions import db, login_manager


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager.init_app(app)

login_manager.login_view = "auth.login"


from models.user import User
from routes.auth import auth
from routes.assessment import assessment
from routes.recommendation import recommendation
from routes.skill_gap import skill_gap
from routes.roadmap import roadmap
from routes.resources import resources
from routes.career_advisor import career_advisor


app.register_blueprint(auth)
app.register_blueprint(assessment)
app.register_blueprint(recommendation)
app.register_blueprint(skill_gap)
app.register_blueprint(roadmap)
app.register_blueprint(resources)
app.register_blueprint(career_advisor)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
@login_required
def dashboard():

    # Get career recommendations
    recommendation_results = calculate_recommendations(current_user)

    top_recommendation = None

    if recommendation_results:
    top_recommendation = recommendation_results[0]

    # Determine career
    career = current_user.career_goal

    if not career or career == "Not Sure":

        if top_recommendation:
            career = top_recommendation["career"]
        else:
            career = "AI/ML Engineer"

    # Career match score
    career_score = 0

    if top_recommendation:
        career_score = top_recommendation["score"]

    # Skill gap analysis
    skill_gap = calculate_skill_gap(
        current_user,
        career
    )

    skill_match = skill_gap["match_percentage"]

    # Roadmap progress
    roadmap_items = RoadmapItem.query.filter_by(
        user_id=current_user.id,
        career=career
    ).all()

    total_roadmap = len(roadmap_items)

    completed_roadmap = sum(
        1 for item in roadmap_items
        if item.completed
    )

    if total_roadmap > 0:
        roadmap_progress = round(
            (completed_roadmap / total_roadmap) * 100
        )
    else:
        roadmap_progress = 0

    # Resources and projects
    resources = get_resources(career)
    projects = get_projects(career)

    # Assessment status
    assessment_complete = all([
        current_user.education,
        current_user.experience,
        current_user.skills,
        current_user.interests,
        current_user.career_goal
    ])

    return render_template(
        "dashboard.html",
        career=career,
        career_score=career_score,
        skill_match=skill_match,
        roadmap_progress=roadmap_progress,
        completed_roadmap=completed_roadmap,
        total_roadmap=total_roadmap,
        resources_count=len(resources),
        projects_count=len(projects),
        top_recommendation=top_recommendation,
        assessment_complete=assessment_complete
    )

print("\n========== REGISTER ROUTE CHECK ==========")

for rule in app.url_map.iter_rules():
    if "register" in rule.rule:
        print("URL:", rule.rule)
        print("ENDPOINT:", rule.endpoint)
        print("METHODS:", rule.methods)

print("==========================================\n")

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)