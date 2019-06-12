"""
This script runs the Wrapper_to_Form application using a development server.
"""

from os import environ

def run_app(port, app):
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', str(port))
    except ValueError:
        PORT = port
    app.run(HOST, PORT)