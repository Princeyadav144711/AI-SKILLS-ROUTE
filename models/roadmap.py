from extensions import db


class RoadmapItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    career = db.Column(
        db.String(150),
        nullable=False
    )

    phase = db.Column(
        db.Integer,
        nullable=False
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    skills = db.Column(
        db.String(500)
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )