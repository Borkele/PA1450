from flask import Flask, render_template, url_for, flash, redirect
import datetime
import os.path

from API import getAPIJson, getAPIXML
from graphGenerator import generateGraph
from forms import graph_timeframe, select_weekday, select_forecast
from timeFrame import translateDateFormat, trimTimeFrame, getWeekdayIndex

app = Flask(__name__)

app.config['SECRET_KEY'] = '734e4610c36703ecb10f7716b7f2140f'
app.config['SESSION_REFRESH_EACH_REQUEST']

@app.route("/")
def index():
    """Return the index page of the website."""
    temperature = getAPIJson("hour", "temperature")

    generateGraph(getAPIJson("day", "temperature"), "day", "temperature", "homePage")
    
    return render_template('homepage.html', temperature = temperature)

@app.route("/custom-graph", methods=["GET", "POST"])
def custom():
    """Return a webpage that lets you create custom graphs."""
    form = graph_timeframe()
    graph_generated = os.path.isfile('static/image/graphs/custom.png')


    if form.validate_on_submit():
        start_date = translateDateFormat(str(form.start_date.data))
        end_date = translateDateFormat(str(form.end_date.data))
        data_type = form.data_type.data
        time_frame = form.time_frame.data
        
        if(start_date < end_date):
            graph_generated = generateGraph(trimTimeFrame(getAPIJson("month", data_type), start_date, end_date), time_frame, data_type, "custom")
            
            if(graph_generated):
                flash("Graph successfully generated! You may have to refresh the page to see it.", 'success')
                return redirect('')
            else:
                flash("Graph generator failed! Please check your inputs.", 'danger')

        else:
            flash("Error: The start date must be before the end date.", 'danger')
    
    return render_template('custom-graph.html', form = form, graph_generated = graph_generated)

@app.route("/summary", methods=["GET", "POST"])
def custom_weekday():
    """Returns a webpage that lets you custom graphs based on a given weekday"""
    form = select_weekday()
    graph_generated = os.path.isfile('static/image/graphs/weekdayGraph.png')


    if form.validate_on_submit():
        weekday = form.weekday.data
        flash("Graph successfully generated! You may have to refresh the page to see it.", 'success')

        #maybe other datatypes than temperatures?
        data_frame =  getAPIJson("month", "temperature")
        weekdayindex = getWeekdayIndex(weekday)
        data_frame = data_frame[data_frame.index.weekday==weekdayindex]
        graph_generated = generateGraph(data_frame, "month", "temperature", "weekdayGraph")

    return render_template('summary.html', form = form, graph_generated = graph_generated) 

@app.route("/forecasts", methods=["GET", "POST"])
def forecasts():
    """Returns a webpage that lets you generate graphs of two different weather forecasts so you can compare them."""
    form = select_forecast()

    if form.validate_on_submit():
        forecast_type = form.forecast_type.data
        flash("Graph successfully generated! You may have to refresh the page to see it.", 'success')
        #TODO generate graphs of the chosen forecast type

    return render_template("forecasts.html", form = form)

@app.route("/test", methods=["GET", "POST"])
def test():
    data_frame = getAPIXML("temperature")
    generateGraph(data_frame, "month", "temperature", "testGraph")
    return render_template('test.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)
