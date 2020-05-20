from flask import Flask, render_template

from API import getAPIJson
from graphGenerator import generateGraph

app = Flask(__name__)

@app.route("/")
def index():
    """Return the index page of the website."""
    temperature = getAPIJson("hour", "temperature")

    generateGraph(getAPIJson("day", "temperature"), "day")
    
    return render_template('homepage.html', temperature = temperature)




if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)
