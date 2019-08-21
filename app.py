from flask import Flask
from flask import request, render_template

app = Flask(__name__)

from acknowledgements import acknowledgements


@app.route('/')
def hello():
    return render_template('index.html', acknowledgements='')

@app.route('/', methods=['POST'])
def formpost():
    text = request.form
    authors = list(text.values())
    acknow = acknowledgements(authors, notex=True)
    return render_template('index.html', acknowledgements=acknow)

if __name__ == '__main__':
    # app.debug = True
    app.run()
