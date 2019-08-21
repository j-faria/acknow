from flask import Flask
from flask import request, render_template

app = Flask(__name__)

from acknowledgements import acknowledgements


@app.route('/')
def hello():
    return render_template('index.html', acknowledgements='')

@app.route('/', methods=['POST'])
def formpost():
    form = request.form
    authors = list(form.values())
    authors = [a.strip() for a in authors]
    acknow = acknowledgements(authors, notex=True,
                              noGEANES='geanes' not in form, 
                              noEPIC='epic' not in form)
    return render_template('index.html', acknowledgements=acknow)

if __name__ == '__main__':
    app.debug = True
    app.run()


