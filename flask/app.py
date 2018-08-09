#!/usr/local/bin/python

from weather import Weather, Unit
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, template_folder='template')

app.config['DEBUG'] = True

@app.route('/weather/<loc>')
def weather_loc(loc):
    weather = Weather(unit=Unit.FAHRENHEIT)
    location = weather.lookup_by_location(loc)
    forecasts = location.forecast
    return "Weather: <br>"+ "&emsp; High: " + forecasts[0].high +"\n" + "Low: " + forecasts[0].low

@app.route('/weather', methods = ['POST', 'GET'])
def weather():
    if request.method == 'POST':
        loc = request.form['zip']
        return redirect(url_for('weather_loc', loc=loc))
    return

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

