from flask import json,jsonify,Flask,flash,redirect,request,render_template,url_for,session
from database import register_user,login_user
import re



app = Flask(__name__)

app.secret_key = 'your-secret-key-123456'
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/register",methods=['GET', 'POST'])
def register():
    if request.method =="POST":
        first_name =  request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        birth_place = request.form['birth_place']
        national_code = request.form['national_code']
        city = request.form['city']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        
        if password != confirm_password :
            return render_template("register.html")
        
        elif len(national_code)!= 10 or not national_code.isdigit():
            return render_template('register.html', error="کد ملی باید ۱۰ رقم باشد")

        elif len(phone) !=11 or not  phone.isdigit():
            return render_template('register.html', error="شماره موبایل باید ۱۱ رقم باشد")
        
        
        success, message = register_user(first_name, last_name, age, birth_place, national_code, city, phone, password)
        if success :
            return redirect(url_for('login'))
        
        else :
            return render_template('register.html', error=message)
        
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        national_code = request.form['national_code']
        password = request.form['password']
        
        user = login_user(national_code, password)
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['first_name'] + ' ' + user['last_name']
            return redirect(url_for('dashboard'))
        
        else :
            return render_template('login.html', error="کد ملی یا رمز عبور اشتباه است")
    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', name=session['user_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
        
        
        
        
        