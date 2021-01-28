import random
from bottle import route, run, template, request


WORD_LISTS = {
    'seedbed1': 'seedbed1',
    'seedbed2': 'seedbed2',
    'seed1': 'seed1',
    'seed2': 'seed2',
    'sprout1': 'sprout1',
    'sprout2': 'sprout2',
    'sprout3': 'sprout3',
    'sapling1': 'sapling1',
}


def get_words(level, number):
    the_file = f'words/{WORD_LISTS[level]}'
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
        return template('index', levels=WORD_LISTS.keys())


run(host='localhost', port=8080)
