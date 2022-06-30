import datetime

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '649b2a0e7b9ceb8646f33f258ce6dee607f1dba3'
#os.urandom(20).hex()
app.permanent_session_lifetime = datetime.timedelta(days=10) #  указать время жизни сессии по дефолту 30 дней

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits')+1 #  обновление даных сессии
    else:
        session['visits'] = 1 # запись данный в сессию
    return f"<h1> Main PAge </h1> <p>Число просмотров:  {session['visits']}"

data = [1,2,3,4]
@app.route("/session")
def session_data():
    session.permanent =True
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True
    return f"<p>session['data']: {session['data']}"

if __name__ == "__main__":
    app.run(debug=True)