from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.secret_key = b'n657t64%^876'


@app.route('/')
def index():
    if 'nickname' in session:
        nickname = session['nickname']
    else:
        nickname = 'somebody'
    counter = 0
    if request.cookies.get('counter'):
        counter = int(request.cookies['counter'])
    response = make_response(render_template('index.html', counter=counter, nickname=nickname))
    response.set_cookie('counter', str(counter + 1))
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return """
         <form action='http://localhost:5000/login', method='POST'>
             <input name="nickname">
             <input type="submit">
         </form>
        """
    elif request.method == 'POST':
        session['nickname'] = request.form['nickname']
        return render_template('logged.html', nickname=session['nickname'])


@app.route('/logout')
def logout():
    result = make_response('You logged out')
    session.pop('nickname', None)
    result.set_cookie('counter', max_age=0)
    return result


if __name__ == '__main__':
    app.run(debug=True)
