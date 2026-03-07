from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class BreakRuleForm(FlaskForm):
    min_shift_hours = DecimalField(
        "Minimum Shift Length (hours)",
        validators=[DataRequired(), NumberRange(min=0.5)],
        places=2,
        description="Break applies if shift is longer than this."
    )
    break_minutes = IntegerField(
        "Break Duration (minutes)",
        validators=[DataRequired(), NumberRange(min=1)]
    )
    submit = SubmitField("Save Rule")