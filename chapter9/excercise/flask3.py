from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    kwargs = {}
    kwargs['thing'] = request.values.get('thing')
    kwargs['height'] = request.values.get('height')
    kwargs['color'] = request.values.get('color')
    return render_template('home.html', **kwargs)


app.run(debug=True)
