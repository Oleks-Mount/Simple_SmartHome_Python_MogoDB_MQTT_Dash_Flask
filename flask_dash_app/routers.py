from flask import render_template,request, redirect, session, flash, url_for
from flask import current_app as app
import os
import smtplib, ssl
from pymongo import MongoClient
import paho.mqtt.client as mqtt
import  paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json


app.config.update(dict(
    DEBUG =True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = '111'
))




@app.route('/')
def home_page():
    return render_template('main_page.html')

@app.route('/security')
def security_page():
    return render_template('camera.html')



@app.route('/feedback', methods = ['POST', 'GET'])
def feedback_page():
    sender_email = os.environ.get('email_gmail')
    receiver_email = 'olleksii112@gmail.com'
    password = os.environ.get('password_gmail')
    if request.method == 'POST':
        with smtplib.SMTP('smtp.gmail.com',587) as server:

            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(sender_email,password)
            subject = request.form['subject_feedback']
            body = request.form['content']
            email_feedback = request.form['email_feedback']
            name_feedback = request.form['Name']
            msg = f'Subject: {subject}\n\n{email_feedback}\n\n{name_feedback}\n\n{body}'.encode('utf-8')

            server.sendmail(sender_email,receiver_email,msg)

    return render_template('email_contact.html')


@app.route('/login', methods = ['GET','POST'])
def admin_page():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif  request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['Logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home_page'))
    return render_template('admin.html' , error = error)

@app.route('/admin_logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect(url_for('home_page'))


@app.route('/get_contact',methods = ['GET','POST'])
def add_contact():
    client = MongoClient('localhost', 27017)
    db = client['SmartHome']
    db_collection = db['Client']
    if request.method == 'POST':
        email_client = request.form['email']
        Fname_client = request.form['Fname']
        Lname_client = request.form['Lname']
        phone_client = request.form['number_phone']
        login = request.form['personal_login']
        password = request.form['personal_password']
        db_collection.insert({'email': email_client,'Fname':Fname_client,'Lname':Lname_client,'phone_number': phone_client, 'login': login, 'password': password})
        flash('Дані успішно записані')
        return redirect(url_for('home_page'))
    return render_template('add_email.html')


