from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2.html')

if __name__ == '__main__':
    app.run(port=8888)