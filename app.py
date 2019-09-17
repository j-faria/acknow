from flask import Flask
from flask import request, render_template

app = Flask(__name__)

from acknowledgements import acknowledgements, acknow

def columnify(iterable):
    strings = [str(x) for x in iterable]
    # pad all the strings to match the widest
    widest = max(len(x)+2 for x in strings)
    padded = [x.ljust(widest) for x in strings]
    return padded

def colprint(iterable, width=72, ret=False): 
    columns = columnify(iterable)
    colwidth = len(columns[0])+2 
    perline = (width-4) // colwidth

    # if ret:
    #     columns = [c.replace(' ', '&nbsp;') for c in columns]
 
    msg = ''
    for i, column in enumerate(columns): 
        if ret:
            msg += column + '&nbsp;&nbsp;'
        else:
            print(column, end=' ') 
        if i % perline == perline-1:
            if ret:
                msg += '</br>'
            else:
                print('\n', end='')
    if ret:
        return msg


known_authors = [n[2] for n in list(acknow.keys())]
known_authors = colprint(known_authors, width=220, ret=True)

@app.route('/')
def hello():
    return render_template('index.html', acknowledgements='', 
                           known_authors=known_authors)

@app.route('/', methods=['POST'])
def formpost():
    form = request.form
    authors = list(form.values())
    authors = [a.strip() for a in authors]
    acknow = acknowledgements(authors, notex=True,
                              noGEANES='geanes' not in form, 
                              noEPIC='epic' not in form)
    return render_template('index.html', acknowledgements=acknow, 
                           known_authors=known_authors)

if __name__ == '__main__':
    app.debug = True
    app.run()


