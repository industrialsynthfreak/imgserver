from bottle import route, run, template, static_file, error, url


@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@route('/')
@route('/index')
def index():
    return template('index.html', url=url)


@error(404)
def error404(error):
    return template('404.html', url=url)


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
