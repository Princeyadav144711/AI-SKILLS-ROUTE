from extensions import db


class Recommendation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    career = db.Column(db.String(150), nullable=False)

    score = db.Column(db.Integer, nullable=False)

    reason = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )