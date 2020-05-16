"""Module for serving an API."""
from flask import Flask, render_template

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return render_template('hello.html')


    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="127.0.0.1", help="The address to listen on")
