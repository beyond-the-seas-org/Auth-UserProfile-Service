from app import db


# Create a model for the table 'student'
class ShortlistModel(db.Model):


    __tablename__ = 'shortlist'

    student_id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, primary_key=True)
   
    
    # create a json method
    def json(self):
        return {
            'student_id': self.student_id,
            'professor_id': self.professor_id
        }