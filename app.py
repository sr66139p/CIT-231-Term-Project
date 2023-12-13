from flask import Flask, render_template, url_for
from json import load as jload

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja2.html')


@app.route('/internet')
def internet():
    return render_template('wifi.jinja2.html')


@app.route('/schedule')
def schedule():
    with open('static/data/courses.json', 'rt') as f:
        data = jload(f)
    return render_template('schedule.jinja2.html', data=data)


@app.route('/about')
def about():
    return render_template('about.jinja2.html')


@app.route('/events')
def events():
    with open('static/data/events.json', 'rt') as f:
        data = jload(f)
    return render_template('events.jinja2.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.jinja2.html')


if __name__ == '__main__':
    app.run(port=8888)
