from db import db

class UserModel(db.Model):
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    password = db.Column(db.String())
    
    @classmethod
    def find_by_username(cls, username):
       return cls.query.filter_by(name=username).first()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

    def save_in_db(self):
        db.session.add(self)
        db.session.commit()
