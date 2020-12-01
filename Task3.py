from flask import Flask, render_template, request, session, make_response, escape

app = Flask(__name__)
app.secret_key = b'n657t64%^876'


@app.route('/')
def index():
    if 'nickname' in session:
        nickname = session['nickname']
    else:
        nickname = 'somebody'
    counter = 0
    if session.get('visited'):
        counter = session['visited']
    else:
        session['visited'] = 0
    response = make_response(render_template('index.html', counter=counter, nickname=nickname))
    session['visited'] += 1
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
    session.pop('nickname', None)
    return f"Your session is clear"


app.run(debug=True)
