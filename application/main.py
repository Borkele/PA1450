from flask import Flask, render_template, url_for, flash, redirect
import datetime

from API import getAPIJson
from graphGenerator import generateGraph
from forms import graph_timeframe

app = Flask(__name__)

app.config['SECRET_KEY'] = '734e4610c36703ecb10f7716b7f2140f'

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

    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
        
        if(start_date < end_date):
            flash("Graph successfully generated!", 'success')
        else:
            flash("Error: The start date must be before the end date.", 'danger')
        return redirect('')
    
        # TODO send date information to the graph generator

    return render_template('custom-graph.html', form = form)





if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)
