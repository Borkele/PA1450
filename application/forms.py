from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, SelectField
from wtforms.validators import data_required

class graph_timeframe(FlaskForm):
    data_type = SelectField('Select weather data', choices=[ ('temperature', 'Temperature'), ('precipitation', 'Precipitation'), ('wind', 'Wind'), ('sight', 'Sight'), ('pressure', 'Air pressure') ])
    start_date = DateField('Start date, format mm/dd/yyyy', format='%m/%d/%Y', validators=[data_required(message="Please enter a date.")])
    end_date = DateField('End date, format mm/dd/yyyy', format='%m/%d/%Y', validators=[data_required(message="Please enter a date.")])
    time_frame = SelectField('Select a time format', choices=[ ('day', 'Day'), ('month', 'Month') ])
    submit = SubmitField('Generate!')

class select_weekday(FlaskForm):
    weekday = SelectField('Select weekday', choices = [('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')])
    submit = SubmitField('Generate!')