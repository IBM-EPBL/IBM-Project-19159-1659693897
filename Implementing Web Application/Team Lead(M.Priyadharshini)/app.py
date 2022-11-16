from flask import *
from twilio.rest import Client
from werkzeug.utils import secure_filename
from flask_ngrok import run_with_ngrok
#import mysql.connector
from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import ibm_db
import os

app = Flask(__name__)
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tpp03734;PWD=kSgr4rTn5rWIthjQ",'','')

import csv

run_with_ngrok(app)
app.secret_key = "your secret key"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        phno = request.form['phno']
        blood_group = request.form['blood_group']
        weight = request.form['weight']
        gender = request.form['gender']
        dob = request.form['dob']
        address = request.form['address']
        adharno = request.form['adharno']
      
        insert_sql = "INSERT INTO Donor1 VALUES (?,?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, email)
        ibm_db.bind_param(prep_stmt, 3, phno)
        ibm_db.bind_param(prep_stmt, 4, blood_group)
        ibm_db.bind_param(prep_stmt, 5, weight)
        ibm_db.bind_param(prep_stmt, 6, gender)
        ibm_db.bind_param(prep_stmt, 7, dob)
        ibm_db.bind_param(prep_stmt, 8, address)
        ibm_db.bind_param(prep_stmt, 9, adharno)
        ibm_db.execute(prep_stmt)
       


    else:
        return render_template("Register.html")



if __name__ == "__main__":
    app.run()
