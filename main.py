import os
import uuid
import urllib
import random
from bottle import route, run, template, request, abort, redirect


LEVELS = os.listdir('words')


def make_id():
    return uuid.uuid4().int


def get_seeded_sample(words, seed, quantity):
    '''
        given words (list of strings), a seed (int) and a quantity (int),
        return a list of size `quantity` from the `words` that will always
        return the same given the same seed
    '''
    random.seed(seed)
    return random.sample(words, quantity)


def get_word_list_from_seed(level, seed, quantity):
    ''' this will return the webpage which is a list of words from a seed'''

    the_file = os.path.join('words', level)

    with open(the_file) as f:
        words = [line for line in f]

    words = get_seeded_sample(words, seed, quantity)
    words = ''.join(words).strip()

    return words


@route('/words/')
def index():
    ''' entry point for all requests '''

    quantity = request.query.quantity
    if quantity:
        quantity = int(quantity)
    else:
        quantity = 10

    level = request.query.level
    if level not in LEVELS:
        level = 'seedbed2'

    if request.query.seed == "get":
        # we hit this path when you submit the form
        params = {k: v[0] for k, v in request.query.dict.items()}
        params['seed'] = make_id()
        params = urllib.parse.urlencode(params)
        redirect('.?' + params)
    elif request.query.seed:
        # we have a seed
        seed = request.query.seed
        words = get_word_list_from_seed(level, seed, quantity)
    else:
        # no seed so no words
        words = []

    return template('index', words=words, levels=LEVELS, quantity=quantity, level=level)


run(host='localhost', port=8080)
