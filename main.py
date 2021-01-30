import os
import uuid
import random
from bottle import route, run, template, request, abort


LEVELS = os.listdir('words')


def make_id():
    return uuid.uuid4().int


def get_words(level, number):
    if level not in LEVELS:
        abort(404)
    the_file = os.path.join('words', level)
    with open(the_file) as f:
        words = [line for line in f]
    words = sorted(random.sample(words, int(number)))
    return template('list', res=words)


@route('/words/')
def index():
    if request.query.level:
        quantity = request.query.quantity
        if quantity:
            quantity = int(quantity)
        else:
            quantity = 10
        return get_words(request.query.level, quantity)
    else:
        return template('index', levels=LEVELS)


run(host='localhost', port=8080)
