#!/usr/bin/env python

import tempfile
import logging
import os

from datetime import datetime, timedelta
from subprocess import Popen, PIPE

from bottle import Bottle, template, static_file, request, response
from gevent.wsgi import WSGIServer

from config import *

__version__ = '1.0.0'

_name_gen = tempfile._get_candidate_names()
_dead_time = timedelta(seconds=DEAD_TIME)
_last_accessed = {'timestamp': None, 'img': None}

_app = Bottle()

logging.basicConfig(filename=LOG, format='%(asctime)-15s: %(message)s',
                    level=logging.INFO, filemode='w')


@_app.get('/')
@_app.get('/index')
def index():

    def generate_unique():
        img = '%s.%s' % (next(_name_gen), IMG_TYPE)
        script = '%s %s/%s' % (SCRIPT_PATH, IMG_PATH, img)
        pipen = Popen(script, shell=True, stdout=PIPE,
                      stderr=PIPE)
        out, err = pipen.communicate()
        if pipen.returncode == 0:
            response.set_cookie('img-token', img, secret=SECRET_KEY)
            _last_accessed['timestamp'] = datetime.utcnow()
            _last_accessed['img'] = img
            logging.info('requested image "%s" from %s' % (img, ip))
            return img
        else:
            logging.error('an error has occurred during the script '
                          'execution: %s' % err)
            return None

    ip = request.environ.get('REMOTE_ADDR')

    img = request.get_cookie('img-token', DEFAULT_IMG, secret=SECRET_KEY)
    if not os.path.exists('%s/%s' % (IMG_PATH, img)):
        img = DEFAULT_IMG

    if request.GET.get('get image'):
        if _last_accessed['timestamp'] and (
                    datetime.utcnow() -_last_accessed['timestamp']
        ) <= _dead_time:
            img = _last_accessed['img']
        else:
            _img = generate_unique()
            if _img:
                img = _img

    logging.info('accessed image "%s" from %s' % (img, ip))
    return template('templates/index.html', img='%s/%s' % (IMG_PATH, img))


@_app.error(404)
def error404(error):
    return template('templates/404.html')


@_app.route('/static/css/<filename:re:.*\.css>')
def static_css(filename):
    return static_file(filename, root='static/css')


@_app.route('/static/img/<filename:re:.*\.(jpe?g|gif|png|ico|svg)>')
def static_img(filename):
    return static_file(filename, root=IMG_PATH)


@_app.route('/static/js/<filename:re:.*\.js>')
def static_js(filename):
    return static_file(filename, root='static/js')


@_app.route('/<filename:re:.*\.txt>')
def static_txt(filename):
    return static_file(filename, root='static')


if __name__ == "__main__":
    logging.info('starting server at %s %d' % (HOST, PORT))
    #_app.run(host=HOST, port=PORT, debug=DEBUG)
    server = WSGIServer((HOST, PORT), _app)
    server.serve_forever()
    logging.info('server shutdown')
