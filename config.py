import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "ai-skills-route-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "database", "ai_skills_route.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False