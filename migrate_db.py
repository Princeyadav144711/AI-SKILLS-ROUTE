
from app import app
from extensions import db
from sqlalchemy import inspect

with app.app_context():

    inspector = inspect(db.engine)

    columns = [
        column["name"]
        for column in inspector.get_columns("user")
    ]

    if "experience" not in columns:

        with db.engine.begin() as connection:
            connection.exec_driver_sql(
                "ALTER TABLE user ADD COLUMN experience VARCHAR(100)"
            )

        print("SUCCESS: Experience column added!")

    else:
        print("Experience column already exists.")
