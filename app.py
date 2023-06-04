# Import all important libraries
import pickle
import pandas as pd
import numpy as np
from itertools import zip_longest
from flask import *
from flask_mysqldb import MySQL
import importlib
# Cursor is a database object to retrieve data from a result set one row at a time
import MySQLdb.cursors
import re  # regular expression
 
#from flask_mail import *
from random import *
import smtplib

# initialize first flask
app = Flask(__name__)
# Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering.

app.secret_key = 'projectwork'
# with open('config.json', 'r') as f:
#     params = json.load(f)['params']
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = '587'
# app.config['MAIL_USERNAME'] = params['gmail-user']
# app.config['MAIL_PASSWORD'] = params['gmail-password']
# app.config['MYSQL_USE_TLS'] = True
# app.config['MYSQL_USE_SSL'] = False
# mail = Mail(app)
otp = randint(100000, 999999) #otp generation
# mysql configuration with flask
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vandit@123'
app.config['MYSQL_DB'] = 'userchurn'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        # cnx = mysql.connector.connect(database='userchurn')
        # cursor = cnx.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM user WHERE email = % s AND password = % s',
            (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            # return render_template('otpverify.html',
            #                        message=message)
            sender_email = "vandittalwadia30@gmail.com"
            sender_pass = "jzxbdxykdhidjjzu"  #app password created after 2step verification google id
            receive_email = user['email']
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email, sender_pass)
            message = """From: """+"Admin"+""" <"""+sender_email+""">
Content-type: text/html
Subject: LOGIN OTP
<h3>Churn Prediction Portal OTP Verification</h3>
<p>Your One Time Password to verify your Account is :</p>
<h4>OTP : """+str(otp)+""" </h4>
<p>Please do not share this code with anyone.</p>
<p>Thankyou!! Have a Nice day.</p>
<h3>Regards ,</h3>
<h3>Vandit</h3>

"""
            s.sendmail(sender_email, receive_email, message)
            s.quit()
            return render_template('enterotp.html')


           
        else:
            message = 'Please enter correct email / password !'
    return render_template('signuplogin.html', message=message)


# @app.route('/enterotp', methods=['GET', 'POST'])
# def enterotp():
#     sender_email = "vandittalwadia30@gmail.com"
#     sender_pass = "errlmtqeftcxyhsl"  #app password created after 2step verification google id
#     receive_email = request.form['email']
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(sender_email, sender_pass)
#     message = """From: """+"Admin"+""" <"""+sender_email+""">
# Content-type: text/html
# Subject: LOGIN OTP
# <h3>Churn Prediction Portal OTP Verification</h3>
# <h4>OTP : """+str(otp)+""" </h4>
# <p>Thankyou!! Have a Nice day.</p>
# """
#     s.sendmail(sender_email, receive_email, message)
#     s.quit()
#     return render_template('enterotp.html')

#validating OTP
@app.route('/validate', methods=['GET','POST'])
def validate():
    userotp = request.form['one']+request.form['two']+request.form['three']+request.form['four']+request.form['five']+request.form['six']
    if otp == (int)(userotp):
        return render_template('home.html')
    return render_template('signuplogin.html', msg='not verified account , try again')

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/bankchurn' , methods=['GET','POST'])
def bankchurn():
    
    
        return render_template('bankchurn.html')
    
@app.route('/predictbank', methods=['POST'])
def predictbank():
    message=''
    if request.method == 'POST' and 'dependentcount' in request.form and 'Total_Relationship_Count' in request.form and 'Months_Inactive_12_mon' in request.form and 'Contacts_Count_12_mon' in request.form and  'Credit_Limit' in request.form and 'Total_Revolving_Bal' in request.form and 'Avg_Open_To_Buy' in request.form and 'Total_Amt_Chng_Q4_Q1' in request.form and 'Total_Trans_Amt'  in request.form and 'Total_Trans_Ct'  in request.form and 'Total_Ct_Chng_Q4_Q1' in request.form and 'Avg_Utilization_Ratio' in request.form and 'Age' in request.form and 'Bank_Relationship_Period' in request.form:
        
        Dependent_count = request.form['dependentcount']
        Total_Relationship_Count=request.form['Total_Relationship_Count']
        Months_Inactive_12_mon=request.form['Months_Inactive_12_mon']
        Contacts_Count_12_mon=request.form['Contacts_Count_12_mon']
        Credit_Limit=request.form['Credit_Limit']
        Total_Revolving_Bal=request.form['Total_Revolving_Bal']
        Avg_Open_To_Buy=request.form['Avg_Open_To_Buy']
        Total_Amt_Chng_Q4_Q1=request.form['Total_Amt_Chng_Q4_Q1']
        Total_Trans_Amt=request.form['Total_Trans_Amt']
        Total_Trans_Ct=request.form['Total_Trans_Ct']
        Total_Ct_Chng_Q4_Q1=request.form['Total_Ct_Chng_Q4_Q1']
        Avg_Utilization_Ratio=request.form['Avg_Utilization_Ratio']
        Age=request.form['Age']
        Bank_Relationship_Period=request.form['Bank_Relationship_Period']
        
        rfc1 = pickle.load(open('fitted_model_1_1_rfc1.pickle', 'rb'))
        
   
        
               

        
        df=pd.read_csv('1_1.csv')
        df=df.drop(['Attrition_Flag'],axis=1)
        num_arr=pd.DataFrame(np.array([[Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period]]),columns=df.columns)
        df_concatnd=pd.concat([df,num_arr],axis=0)
        df_concatnd.reset_index(drop=True,inplace=True)
        df_concatnd_last=df_concatnd.iloc[-1,:]
        prediction=rfc1.predict(np.array([df_concatnd_last]))
        if(prediction[0]==1):
            message='Customer will exit'
        else:
            message='Customer will not exit'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO bankcustomerdetail VALUES (NULL, % s, % s, % s,% s, % s, % s,% s, % s, % s,% s, % s, % s,% s, % s,%s)',(Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon,
                     Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period , message ))
        mysql.connection.commit()
        
        array=[Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon,
                     Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period , message]
       
        headings=['Dependent_count', 'Total_Relationship_Count','Months_Inactive_12_mon', 'Contacts_Count_12_mon',
                     'Credit_Limit','Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1','Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio', 'Age', 'Bank_Relationship_Period', 'Predicted Result']
       
    return render_template('bankchurn.html',myzip=zip_longest(headings,array),message=message)
@app.route('/predictcredit', methods=['POST'])
def predictcredit():
    message=''
    if request.method == 'POST' and 'edu' in request.form and 'marry' in request.form and 'gen' in request.form and 'card'in request.form and 'dependentcount' in request.form and 'Total_Relationship_Count' in request.form and 'Months_Inactive_12_mon' in request.form and 'Contacts_Count_12_mon' in request.form and  'Credit_Limit' in request.form and 'Total_Revolving_Bal' in request.form and 'Avg_Open_To_Buy' in request.form and 'Total_Amt_Chng_Q4_Q1' in request.form and 'Total_Trans_Amt'  in request.form and 'Total_Trans_Ct'  in request.form and 'Total_Ct_Chng_Q4_Q1' in request.form and 'Avg_Utilization_Ratio' in request.form and 'Age' in request.form and 'Bank_Relationship_Period' in request.form:
        Education = request.form['edu']
        Marry = request.form['marry']
        gender = request.form['gen']
        card = request.form['card']
        Dependent_count = request.form['dependentcount']
        Total_Relationship_Count=request.form['Total_Relationship_Count']
        Months_Inactive_12_mon=request.form['Months_Inactive_12_mon']
        Contacts_Count_12_mon=request.form['Contacts_Count_12_mon']
        Credit_Limit=request.form['Credit_Limit']
        Total_Revolving_Bal=request.form['Total_Revolving_Bal']
        Avg_Open_To_Buy=request.form['Avg_Open_To_Buy']
        Total_Amt_Chng_Q4_Q1=request.form['Total_Amt_Chng_Q4_Q1']
        Total_Trans_Amt=request.form['Total_Trans_Amt']
        Total_Trans_Ct=request.form['Total_Trans_Ct']
        Total_Ct_Chng_Q4_Q1=request.form['Total_Ct_Chng_Q4_Q1']
        Avg_Utilization_Ratio=request.form['Avg_Utilization_Ratio']
        Age=request.form['Age']
        Bank_Relationship_Period=request.form['Bank_Relationship_Period']
        
        rfc1 = pickle.load(open('fitted_model_1_1_rfc1.pickle', 'rb'))
        
   
        # x=predicting(Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon,
        #             Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period)
       
               

        
        df=pd.read_csv('1_1.csv')
        df=df.drop(['Attrition_Flag'],axis=1)
        num_arr=pd.DataFrame(np.array([[Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period]]),columns=df.columns)
        df_concatnd=pd.concat([df,num_arr],axis=0)
        df_concatnd.reset_index(drop=True,inplace=True)
        df_concatnd_last=df_concatnd.iloc[-1,:]
        prediction=rfc1.predict(np.array([df_concatnd_last]))
        if(prediction[0]==1):
            message='Customer will exit'
        else:
            message='Customer will not exit'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO creditcustomerdetail VALUES (NULL, % s, % s, % s,% s, % s, % s, % s,% s, % s, % s,% s, % s, % s,% s, % s, % s,% s, % s,%s)',(Education,Marry,gender,card,Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon,
                     Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period , message ))
        mysql.connection.commit()
        
        array=[Education,Marry,gender,card,Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon,
                     Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period , message]
       
        headings=['Education Status','Marital Status','Gender','Card Type','Dependent_count', 'Total_Relationship_Count','Months_Inactive_12_mon', 'Contacts_Count_12_mon',
                     'Credit_Limit','Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1','Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio', 'Age', 'Bank_Relationship_Period', 'Predicted Result']
    return render_template('creditchurn.html',myzip=zip_longest(headings,array),message=message)

    

@app.route('/creditchurn')
def creditchurn():
    return render_template('creditchurn.html')


@app.route('/bankviz')
def bankviz():
    return render_template('bankviz.html')
@app.route('/creditviz')
def creditviz():
    return render_template('creditviz.html')
# Make function for logout session


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:

        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s',
                       (email, ))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address !'
        elif not userName or not password or not email:
            message = 'Please fill out the form !'
        else:
            cursor.execute(
                'INSERT INTO user VALUES (NULL, % s, % s, % s)',
                (userName, email, password, ))
            mysql.connection.commit()
            message = 'You have successfully registered ! Please Sign in to Continue'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('signuplogin.html', message=message)







# run code in debug mode
if __name__ == "__main__":
    app.run(debug=True)
