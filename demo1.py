from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = 'jumpjacks'

email_id = ''
user = model.check_users()
@app.route('/', methods= ['GET'])
def home():
    if 'email_id' in session:
        g.user= session['email_id']
        return render_template('showpage.html')
        #, message = '<img src= static/img/pic.jpg>')

    return render_template('homepage.html',message = 'Login to the page or sign up!') 
@app.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == 'POST':
        session.pop('email_id',None)
        areyouuser = request.form['email_id']
        pwd = model.check_pw(areyouuser)

        if request.form['password'] == pwd:
            session['email_id'] = request.form['email_id']
        return redirect(url_for('home'))   

    return render_template('index.html')       
@app.before_request
def before_request():
    g.email_id = None
    if 'email_id' in session:
        g.email_id = session['email_id']
@app.route('/about', methods = ['GET']) 
def about():
        return render_template('about.html')   
@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up!!'
        return render_template('signup.html', message = message)  
    else:
        email_id = request.form["email_id"]
        password = request.form["password"]   
        message = model.signup(email_id,password)
        return render_template('signup.html', message = message)        
@app.route('/getsession')
def getsession():
        if 'email_id' in session:
            return session['email_id']
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
        session.pop('email_id',None)
        return redirect(url_for('home'))    
@app.route('/Terms_of_Use', methods = ['GET'])
def Terms_of_use():
        return render_template('Terms_of_Use.html')           
@app.route('/Privacy', methods = ['GET'])
def Privacy():
        return render_template('Privacy.html')     
@app.route('/dashboard.html', methods = ['GET','POST'])
def dashboard():
        return render_template('dashboard.html')

@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        Listname = request.form['listname']
        taskname = request.form['taskname']        
        mydata = Model.add_to_list(Listname,taskname)
        rows = Model.getalltask()   
        return render_template(url_for('showpage.html', rows = rows))                          

if __name__ == '__main__':
    app.run(debug = True)    