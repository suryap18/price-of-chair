from src.app import app

__author__ = 'jslvtr'

if __name__ == "main":
    app.run(debug=app.config['DEBUG'], port=4990)
