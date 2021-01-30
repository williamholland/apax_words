import os
import uuid
import random
from bottle import route, run, template, request, abort


LEVELS = os.listdir('words')


def make_id():
    return uuid.uuid4().int


def get_word_list():
    ''' this will return the webpage which is a list of words '''
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
    words = sorted(random.sample(words, int(quantity)))
    return template('list', res=words)


def get_homepage_form():
    ''' this will return the webpage for the search form '''
    return template('index', levels=LEVELS)


@route('/words/')
def index():
    ''' entry point for all requests '''
    if request.query.level:
        # if level is passed then we want a list of words
        return get_word_list()
    else:
        # otherwise we go to the landing page
        return template('index', levels=LEVELS)
        return get_homepage_form()


run(host='localhost', port=8080)
