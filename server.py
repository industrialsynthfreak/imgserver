from bottle import route, run, template


@route('/')
@route('/index')
def index():
    return template('index.html')


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
