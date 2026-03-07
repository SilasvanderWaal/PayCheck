from app.extensions import db

class BreakRule(db.Model):
    __tablename__ = "break_rules"

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=False)

    min_shift_hours = db.Column(db.Numeric(4, 2), nullable=False)
    break_minutes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<BreakRule >{self.min_shift_hours}h -> {self.break_minutes}min>"
    
    