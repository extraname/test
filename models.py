from settings import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(10))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender
        }


def serialize_multiple(objects: list) -> list:
    return [obj.serialize() for obj in objects]


if __name__ == '__main__':
    db.create_all()
