import random
from bottle import route, run, template


TEMPLATE = '''
%for item in res:
    {{item}}
    <br/>
%end
'''

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/words/<level>/<number>/')
def get_words(level, number):
    with open(f'words/{level}') as f:
        words = [line for line in f]
    words = sorted(random.sample(words, int(number)))
    return template(TEMPLATE, res=words)

run(host='localhost', port=8080)
