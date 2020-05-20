from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import data_required

class graph_timeframe(FlaskForm):
    start_date = DateField('Start date, format mm/dd/yyyy', format='%m/%d/%Y', validators=[data_required(message="Please enter a date.")])
    end_date = DateField('End date, format mm/dd/yyyy', format='%m/%d/%Y', validators=[data_required(message="Please enter a date.")])
    submit = SubmitField('Generate!')