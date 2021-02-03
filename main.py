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


def get_word_list_from_seed(seed):
    ''' this will return the webpage which is a list of words from a seed'''
    quantity = request.query.quantity
    if quantity:
        quantity = int(quantity)
    else:
        quantity = 10
    level = request.query.level
    if level not in LEVELS:
        abort(404)
    the_file = os.path.join('words', level)
    with open(the_file) as f:
        words = [line for line in f]
    words = get_seeded_sample(words, seed, quantity)
    return template('list', res=words, levels=LEVELS, quantity=quantity, level=level)


def get_homepage_form():
    ''' this will return the webpage for the search form '''
    return template('index', levels=LEVELS)


@route('/words/')
def index():
    ''' entry point for all requests '''
    if request.query.seed:
        seed = request.query.seed
        return get_word_list_from_seed(seed)
    elif request.query.level and request.query.quantity:
        params = {k: v[0] for k, v in request.query.dict.items()}
        params['seed'] = make_id()
        params = urllib.parse.urlencode(params)
        redirect('.?' + params)
    else:
        # otherwise we go to the landing page
        return template('index', levels=LEVELS)
        return get_homepage_form()


run(host='localhost', port=8080)
