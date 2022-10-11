from extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
        is_active = db.Column(db.Boolean(), default=False)
        created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    default=db.func.now())
        updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

