from flask import Flask, render_template
from parsing_currency import *
from parsing_afisha2 import *
from parsing_weather import *

from paste import app

from paste.controllers.helpers import render

app = Flask(__name__)

@app.route('/comments/')
def root():
    return render('index')


@app.route('/')
def courses():
    return render_template('currency.html', NameCur=name, Cur=rate)


@app.route('/movies/')
def movies():
    return render_template('movie.html', afis=main())


@app.route('/weather/')
def weather():
    return render_template('weather.html', weatday=Weather_day(), weattemp=Weather_temp())


if __name__ == '__main__':
    app.run(debug=True)
