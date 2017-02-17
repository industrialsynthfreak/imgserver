#!/usr/bin/env python

import tempfile
import logging

from subprocess import Popen, PIPE

from bottle import Bottle, template, static_file, request, response

from config import *

_name_gen = tempfile._get_candidate_names()
_app = Bottle()
logging.basicConfig(filename=LOG, format='%(asctime)-15s: %(message)s',
                    level=logging.INFO)


@_app.route('/static/css/<filename:re:.*\.css>')
def static_css(filename):
    return static_file(filename, root='static/css')


@_app.route('/%s/<filename:re:.*\.(jpe?g|gif|png|ico|svg)>' % IMG_PATH)
def static_img(filename):
    return static_file(filename, root='static/img')


@_app.route('/static/js/<filename:re:.*\.js>')
def static_js(filename):
    return static_file(filename, root='static/js')


@_app.route('/<filename:re:.*\.txt>')
def static_txt(filename):
    return static_file(filename, root='static')


@_app.get('/')
@_app.get('/index')
def index():
    img = request.get_cookie('img-token', secret=SECRET_KEY)
    ip = request.environ.get('REMOTE_ADDR')
    if request.GET.get('get image'):
        img = '%s.jpg' % next(_name_gen)
        script = '%s %s/%s' % (SCRIPT_PATH, IMG_PATH, img)
        out, err = Popen(script, shell=True, stdout=PIPE,
                         stderr=PIPE).communicate()
        if not err:
            response.set_cookie('img-token', img, secret=SECRET_KEY)
            logging.info('requested image "%s" from %s' % (img, ip))
        else:
            logging.error('an error has occurred during the script execution')
    elif not img:
        img = DEFAULT_IMG
    else:
        logging.error('accessed image "%s" from %s' % (img, ip))
    return template('index.html', img='%s/%s' % (IMG_PATH, img))


@_app.error(404)
def error404(error):
    return template('404.html')


if __name__ == "__main__":
    _app.run(host=HOST, port=PORT, debug=DEBUG)
